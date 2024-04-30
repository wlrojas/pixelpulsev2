from django.contrib import messages
import requests
from django.shortcuts import render
from django.shortcuts import redirect
from .utils import obtener_tasa_de_cambio, obtener_clima
from pixelpulsegaming.models import Productos


def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {
            'username': username,
            'password': password
        }
        try:
            response = requests.post('http://localhost:8000/usuario/inicio/', data=data)
            if response.status_code == 200:
                redirect_response = redirect('index')
                token = response.json().get('token')
                redirect_response.set_cookie(
                    'auth_token',
                    token,
                    httponly=True,
                    max_age=3600
                )
                return redirect_response
            else:
                messages.error(request, 'Error al iniciar sesión')
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Error al conectar con el servicio de autenticación: {str(e)}')

    return render(request, 'iniciarSesion.html')


def crear_cuenta(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
        }

        response = requests.post('http://localhost:8000/usuario/registro/', data=data)

        if response.status_code == 200:
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('login')
        else:
            messages.error(request, 'Error al registrar cuenta: ' + response.text)
    else:
        return render(request, 'crearCuenta.html')

    return render(request, 'crearCuenta.html')


def index(request):
    clima = obtener_clima
    return render(request, 'index.html', {'clima': clima})


def categoria(request):
    return render(request, 'categoria.html')


def monitores(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Monitores")
    return render(request, 'CATEGORIAS_HTML/monitores.html', {'productos': productos})


def notebooks(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Notebooks")
    return render(request, 'CATEGORIAS_HTML/notebooks.html', {'productos': productos})


def perifericos(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Periféricos")
    return render(request, 'CATEGORIAS_HTML/perifericos.html', {'productos': productos})


def procesadores(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Procesadores")
    return render(request, 'CATEGORIAS_HTML/procesadores.html', {'productos': productos})


def sillasGamer(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Sillas Gamer")
    return render(request, 'CATEGORIAS_HTML/sillasGamer.html', {'productos': productos})


def tarjetasDeVideo(request):
    productos = Productos.objects.filter(categoria__nombreCategoria="Tarjetas de Video")
    return render(request, 'CATEGORIAS_HTML/tarjetasDeVideo.html', {'productos': productos})


def perfil(request):
    return None


def agregar_a_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    key = str(producto_id)
    cantidad = carrito.get(key, 0)
    carrito[key] = cantidad + 1
    request.session['carrito'] = carrito
    return redirect('carrito')


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
    request.session['carrito'] = carrito
    return redirect('carrito')


def actualizar_carrito(request, producto_id, cantidad):
    carrito = request.session.get('carrito', {})
    if cantidad == 0:
        del carrito[producto_id]
    else:
        carrito[producto_id] = cantidad
    request.session['carrito'] = carrito
    return redirect('carrito')


def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('carrito')


def mostrar_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0
    moneda_actual = request.session.get('moneda_actual', 'CLP')
    tasa = obtener_tasa_de_cambio('CLP', moneda_actual)
    for producto_id, cantidad in carrito.items():
        producto = Productos.objects.get(idProducto=producto_id)
        subtotal = (producto.precio * cantidad) * tasa
        items.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'carrito.html', {'items': items, 'total': total, 'moneda_actual': moneda_actual})


def cambiar_moneda(request):
    moneda = request.GET.get('moneda', 'CLP')
    request.session['moneda_actual'] = moneda
    return redirect(request.META.get('HTTP_REFERER', 'vista_carrito'))
