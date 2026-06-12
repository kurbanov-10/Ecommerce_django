from django.urls import path

from apps.products.views import get_products
from apps.products.api_endpoints.products.Productlist.views import product_list
from apps.products.api_endpoints.products.ProductUpdate.views import update_product


urlpatterns = [
    path("api/products/", product_list, name="api_product_list"),
    path("products/", get_products, name="product_list"),
    path("api/products/<int:pk>/", update_product, name="api_product_update"),
]