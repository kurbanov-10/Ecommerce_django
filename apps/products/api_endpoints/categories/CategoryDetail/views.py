from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from apps.products.api_endpoints.categories.CategoryDetail.serializers import CategoryDetailSerializer
from apps.products.models import Category

# @api_view(['GET'])
# def category_detail_view(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except:
#         return Response({'error': 'Category not found'}, status=404)
    
#     serializer = CategoryDetailSerializer(category)
#     return Response(serializer.data)

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer