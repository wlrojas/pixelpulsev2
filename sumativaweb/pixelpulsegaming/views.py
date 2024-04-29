from django.contrib import messages
import requests
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.


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
    return render(request, 'index.html')


def categoria(request):
    return render(request, 'categoria.html')


def monitores(request):
    return render(request, 'CATEGORIAS_HTML/monitores.html')


def notebooks(request):
    return render(request, 'CATEGORIAS_HTML/notebooks.html')


def perifericos(request):
    return render(request, 'CATEGORIAS_HTML/perifericos.html')


def procesadores(request):
    return render(request, 'CATEGORIAS_HTML/procesadores.html')


def sillasGamer(request):
    return render(request, 'CATEGORIAS_HTML/sillasGamer.html')


def tarjetasDeVideo(request):
    return render(request, 'CATEGORIAS_HTML/tarjetasDeVideo.html')





def perfil(request):
    return None