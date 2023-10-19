from django.shortcuts import render
from .models import Products

def index(request):
    produtos = Products.objects.all()
    return render(request, 'pages/index.html', {'produtos':produtos})


