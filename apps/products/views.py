from django.shortcuts import render
from apps.products.models import Category, Product

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products":products})

def get_category(request):
    category = Category.objects.all()
    return render(request, "category/list.html", {"category":category})

