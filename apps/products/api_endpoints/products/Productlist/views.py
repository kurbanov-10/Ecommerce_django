from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.Productlist.serializers import ProductlistSerializer
from apps.products.models import Product



@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductlistSerializer(products, many=True)
    return Response(serializer.data)