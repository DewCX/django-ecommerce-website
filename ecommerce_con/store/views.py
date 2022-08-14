from django.shortcuts import render
from .models import *


#Store view
def store(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, 'store/store.html', context)


#Cart View
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


#Checkout view
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context) 