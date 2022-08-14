from django.shortcuts import render



#Store view
def store(request):
    context = {}
    return render(request, 'store/store.html', context)


#Cart View
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


#Checkout view
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context) 