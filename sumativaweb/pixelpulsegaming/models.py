from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.


class Categorias(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombreCategoria


class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio del producto')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción del producto')

    def __str__(self):
        return self.nombreProducto


class CarritoItem(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio
