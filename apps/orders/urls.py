from django.urls import path

from apps.orders.api_endpoints.orders.Orderlist.views import order_list_view
from apps.orders.api_endpoints.orders.OrderCreate.views import order_create_view
from apps.orders.api_endpoints.orders.OrderDetail.views import order_detail_view
from apps.orders.api_endpoints.orders.OrderUpdate.views import order_update_view


urlpatterns = [
    path("get_orders/", order_list_view, name="order_list"),
    path("create_order/", order_create_view, name="order_create"),
    path("order_detail/<int:pk>/", order_detail_view, name="order_detail"),
    path("order_update/<int:pk>/", order_update_view, name="order_update"),
    path("order_delete/<int:pk>/", order_update_view, name="order_delete"),
]