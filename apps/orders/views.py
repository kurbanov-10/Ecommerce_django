from django.shortcuts import render

from apps.orders.models import Order

def get_orders(request):
    orders = Order.objects.all()
    return render(request, "orders/list.html", {"orders":orders})