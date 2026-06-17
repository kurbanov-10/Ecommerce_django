from django.urls import path

from apps.products.views import get_category
from apps.products.api_endpoints.categories.CategoryCreate.views import CategoryCreateAPIView
from apps.products.api_endpoints.categories.CategoryDetail.views import CategoryDetailAPIView
from apps.products.api_endpoints.categories.CategoryUpdate.views import CategoryDeleteView, CategoryUpdateView
from apps.products.api_endpoints.categories.Categorylist.views import CategoryListAPIView
from apps.products.views import get_products
from apps.products.api_endpoints.products.Productlist.views import ProductListAPIView
from apps.products.api_endpoints.products.ProductCreate.views import ProductCreateAPIView
from apps.products.api_endpoints.products.ProductUpdate.views import ProductUpdateAPIView, ProductDeleteAPIView
from apps.products.api_endpoints.products.ProductDetail.views import ProductDetailAPIView


urlpatterns = [
    path("", get_products, name="get_products"),
    path("api/list/", ProductListAPIView.as_view(), name="product_list"),
    path("api/create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("api/update/<int:pk>/", ProductUpdateAPIView.as_view(), name="product_update"),
    path("api/delete/<int:pk>/", ProductDeleteAPIView.as_view(), name="product_delete"),
    path("api/detail/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail"),
    path("", get_category, name="category_list"),
    path("api/list/", CategoryListAPIView.as_view(), name="category_list"),
    path("api/create/", CategoryCreateAPIView.as_view(), name="category_create"),
    path("api/update/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
    path("api/delete/<int:pk>/", CategoryDeleteView.as_view(), name="category_delete"),
    path("api/<int:pk>/", CategoryDetailAPIView.as_view(), name="category_detail"),
]