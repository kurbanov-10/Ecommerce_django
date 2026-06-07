from django.urls import path

from apps.category.views import get_category

urlpatterns = [
    path("category/", get_category, name="category_list")
]
