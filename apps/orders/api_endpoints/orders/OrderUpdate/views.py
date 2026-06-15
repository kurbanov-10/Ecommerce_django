from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, DestroyAPIView

from apps.orders.api_endpoints.orders.OrderCreate.serializers import OrderCreateSerializer
from apps.orders.models import Order

# @api_view(['PATCH', 'DELETE'])
# def order_update_view(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#     except:
#         return Response({'error': 'Order not found'}, status=404)
    
#     if request.method == 'PATCH':
#         serializer = OrderCreateSerializer(order, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         order.delete()
#         return Response(status=204)

class OrderUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    
class OrderDeleteAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer