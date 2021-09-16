from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'home.html', context)

def product(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'product.html', context)

def cart(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'cart.html', context)

def checkout(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'checkout.html', context)