from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductUpdate.serializers import ProductUpdateSerializer
from apps.products.models import Product

@api_view(['PATCH', 'DELETE'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=404)

    if request.method == 'PATCH':
        serializer = ProductUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)
