from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoints.orders.OrderCreate.serializers import OrderCreateSerializer
from apps.orders.models import Order

@api_view(['GET'])
def order_detail_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except:
        return Response({'error': 'Order not found'}, status=404)
    
    serializer = OrderCreateSerializer(order)
    return Response(serializer.data)