"""
URL configuration for sumativaweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pixelpulsegaming import views, apiViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('iniciarsesion/', views.iniciarsesion, name='login'),
    path('registro/', views.crear_cuenta, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('usuario/', include('usersesion.urls'), name='usuario_sesion'),
    path('categorias/', include('pixelpulsegaming.urls'), name='categorias'),
    path('carrito/', views.mostrar_carrito, name='carrito'),
    path('carrito/vaciar', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/agregar/<int:producto_id>', views.agregar_a_carrito, name='agregar_a_carrito'),
    path('carrito/actualizar/<int:producto_id>/<int:cantidad>', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:producto_id>', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/cambiar_moneda', views.cambiar_moneda, name='cambiar_moneda'),
    path('api/productos', apiViews.list_productos, name='api_productos'),
    path('api/categorias', apiViews.list_categorias, name='api_categorias'),
]
