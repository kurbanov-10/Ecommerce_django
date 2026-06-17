from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.products.api_endpoints.categories.Categorylist.serializers import CategorylistSerializer
from apps.products.models import Category

# @api_view(['GET'])
# def category_list(request):
#     category = Category.objects.all()
#     serializer = CategorylistSerializer(category, many=True)
#     return Response(serializer.data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorylistSerializer