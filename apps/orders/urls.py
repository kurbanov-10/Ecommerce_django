from django.urls import path

from apps.orders.api_endpoints.orders.Orderlist.views import order_list


urlpatterns = [
    path("get_orders/", order_list, name="order_list"),
]