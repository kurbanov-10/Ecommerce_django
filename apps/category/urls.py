from django.urls import path

from apps.category.views import get_category
from apps.category.api_endpoints.categories.Categorylist.views import category_list
from apps.category.api_endpoints.categories.CategoryCreate.views import category_create_view
from apps.category.api_endpoints.categories.CategoryUpdate.views import category_update_view
from apps.category.api_endpoints.categories.CategoryDetail.views import category_detail_view

urlpatterns = [
    path("", get_category, name="category_list"),
    path("api/list/", category_list, name="api_category_list"),
    path("api/create/", category_create_view, name="api_category_create"),
    path("api/update/<int:pk>/", category_update_view, name="api_category_update"),
    path("api/delete/<int:pk>/", category_update_view, name="api_category_delete"),
    path("api/<int:pk>/", category_detail_view, name="api_category_detail"),
]
