from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.products.api_endpoints.products.Productlist.serializers import ProductlistSerializer
from apps.products.models import Product



# @api_view(['GET'])
# def product_list_view(request):
#     products = Product.objects.all()
#     serializer = ProductlistSerializer(products, many=True)
#     return Response(serializer.data)

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializer