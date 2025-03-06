from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
