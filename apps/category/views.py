from django.shortcuts import render
from apps.category.models import *
from apps.products.models import *

def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    
    data = {
        'products': products,
        'category': category,
    }
    return render(request, 'common/home.html', data)
    