from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.category.api_endpoints.categories.Categorylist.serializers import CategorylistSerializer
from apps.category.models import Category

@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorylistSerializer(category, many=True)
    return Response(serializer.data)