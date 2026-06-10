from django.urls import path

from apps.category.views import get_category
from apps.category.api_endpoints.categories.Categorylist.views import category_list

urlpatterns = [
    path("category/", get_category, name="category_list"),
    path("api/category/", category_list, name="api_category_list"),
]
