from django.shortcuts import render
from apps.products.models import Product
from apps.products.models import Category


def home(request):
    context = {
        "products": Product.objects.all()[:8],
        "categories": Category.objects.all()[:6]
    }
    return render(request, "common/home.html", context)