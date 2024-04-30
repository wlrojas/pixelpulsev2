from rest_framework import generics
from .models import Categorias, Productos
from .serializers import CategoriasSerializer, ProductoSerializer


class CategoriaList(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProductoList(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
