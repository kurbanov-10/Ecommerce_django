from django.shortcuts import render
from apps.products.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "common/home.html", {"products":products})