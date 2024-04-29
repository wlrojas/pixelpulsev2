from django.contrib import admin
from .models import Categorias, Productos
from django.contrib.auth.models import AbstractUser


# Register your models here.

admin.site.register(Categorias)
admin.site.register(Productos)
