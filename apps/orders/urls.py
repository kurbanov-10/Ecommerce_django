from django.urls import path

from apps.orders.api_endpoints.orders.Orderlist.views import OrderListAPIView
from apps.orders.api_endpoints.orders.OrderCreate.views import OrderCreateAPIView
from apps.orders.api_endpoints.orders.OrderDetail.views import OrderDetailAPIView
from apps.orders.api_endpoints.orders.OrderUpdate.views import OrderUpdateAPIView, OrderDeleteAPIView


urlpatterns = [
    path("get_orders/", OrderListAPIView.as_view(), name="order_list"),
    path("create_order/", OrderCreateAPIView.as_view(), name="order_create"),
    path("api/detail/<int:pk>/", OrderDetailAPIView.as_view(), name="order_detail"),
    path("api/update/<int:pk>/", OrderUpdateAPIView.as_view(), name="order_update"),
    path("api/delete/<int:pk>/", OrderDeleteAPIView.as_view(), name="order_delete"),
]