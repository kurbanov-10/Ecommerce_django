from django.urls import path

from apps.products.views import get_products
from apps.products.api_endpoints.products.Productlist.views import product_list
from apps.products.api_endpoints.products.ProductCreate.views import create_product
from apps.products.api_endpoints.products.ProductUpdate.views import update_product
from apps.products.api_endpoints.products.ProductDetail.views import product_detail


urlpatterns = [
    path("", get_products, name="product_list"),
    path("api/list/", product_list, name="api_product_list"),
    path("api/create/", create_product, name="api_product_create"),
    path("api/update/<int:pk>/", update_product, name="api_product_update"),
    path("api/delete/<int:pk>/", update_product, name="api_product_delete"),
    path("api/<int:pk>/", product_detail, name="api_product_detail"),
]