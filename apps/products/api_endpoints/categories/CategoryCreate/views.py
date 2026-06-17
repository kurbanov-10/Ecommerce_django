from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apps.products.api_endpoints.categories.CategoryCreate.serializers import CategoryCreateSerializer
from apps.products.models import Category

# @api_view(['POST'])
# def category_create_view(request):
#     serializer = CategoryCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer