from django.shortcuts import render
from .models import Products

def index(request):
    produtos = Products.objects.all()
    return render(request, 'pages/index.html', {'produtos':produtos})

def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product':product})
