from django.urls import path
from usersesion import views

urlpatterns = [
    path('registro/', views.registro, name='registro_usuario'),
    path('inicio/', views.login, name='inicio_usuario'),
]
