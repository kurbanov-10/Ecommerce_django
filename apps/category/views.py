from django.shortcuts import render
from apps.category.models import Category

def get_category(request):
    category = Category.objects.all()
    return render(request, "category/list.html", {"category":category})
