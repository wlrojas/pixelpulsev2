from rest_framework import serializers
from .models import Categorias, Productos


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['idCategoria', 'nombreCategoria']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['idProducto', 'nombreProducto', 'categoria', 'precio', 'descripcion']
