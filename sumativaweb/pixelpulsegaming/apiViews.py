from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Categorias, Productos
from .serializers import CategoriasSerializer, ProductoSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_categorias(request):
    categorias = Categorias.objects.all()
    serializer = CategoriasSerializer(categorias, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_productos(request):
    productos = Productos.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)
