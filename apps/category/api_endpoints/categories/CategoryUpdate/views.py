from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.category.api_endpoints.categories.CategoryUpdate.serializers import CategoryUpdateSerializer
from apps.category.models import Category

@api_view(['PATCH', 'DELETE'])
def category_update_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except:
        return Response({'error': 'Category not found'}, status=404)
    
    if request.method == 'PATCH':
        serializer = CategoryUpdateSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)