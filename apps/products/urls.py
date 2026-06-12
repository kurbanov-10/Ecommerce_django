from django.urls import path

from apps.products.views import get_products
from apps.products.api_endpoints.products.Productlist.views import product_list_view
from apps.products.api_endpoints.products.ProductCreate.views import create_product_view
from apps.products.api_endpoints.products.ProductUpdate.views import update_product_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view


urlpatterns = [
    path("", get_products, name="get_products"),
    path("api/list/", product_list_view, name="product_list"),
    path("api/create/", create_product_view, name="product_create"),
    path("api/update/<int:pk>/", update_product_view, name="product_update"),
    path("api/delete/<int:pk>/", update_product_view, name="product_delete"),
    path("api/<int:pk>/", product_detail_view, name="product_detail"),
]