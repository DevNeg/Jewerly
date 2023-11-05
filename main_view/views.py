from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart, Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from base.defs import prod_suggest,sum_price_prod


def home(request):
    product = Product.objects.all()
    context = {
        'product':product
        }
    return render(request, 'site.html', context)

@login_required(login_url = 'render_login')
def render_cart(request):
    try:
        cart = Cart.objects.get(user = request.user)
        products = Product.objects.filter(cart = cart)
        if len(products) == 0:
            products =0
        total_price = sum_price_prod(products)
        context = {
            'cart':cart,
            'products':products,
            'total_price':total_price,
        }
        return render(request, 'cart.html',context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

@login_required(login_url = 'render_login')
def render_profile(request):
    try:
        historic = Historic.objects.get(user = request.user)
        hist_products = Product.objects.filter(historic = historic)
        if len(hist_products) == 0:
            hist_products = 0#User have no historic buy, so we send a message on his profile
        suggestion_products = prod_suggest(hist_products)
        context = {
            'hist_products':hist_products,
            'suggestion_products':suggestion_products,
        }
        return render(request,'profile.html',context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

def render_jew(request, id):
    try:
        product = Product.objects.get(id = id)
        if product is not None:
            context = {
                'product':product,
            }
            return render(request, 'product.html',context)
        else:
            messages.add_message(constants.WARNING, 'Este produto não existe')
            return redirect('main')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')



    
