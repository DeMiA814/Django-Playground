from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse

from .models import Person, Item, History, Cart
from .forms import Product_form, Login_form

from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    products = Item.objects.all()
    params = {
        'products':products,
    }
    return render(request, 'ecom/index.html', params)

def login(request):
    params = {
        'login':Login_form
    }

    if request.method == "POST":
        authentication(request)
    return render(request, 'ecom/login.html', params)

def authentication(request):
    form = Login_form(data=request.POST)
    if form.is_valid():
        return redirect('views.index')
    form.add_error(None, '入力内容が違います。')

def product(request):
    cart = get_cart()
    number = 0
    product_name = request.GET.get('product')
    product = Item.objects.get(product=product_name)
    params = {
            'product':product,
            'form':Product_form(),
            'number':number,
        }

    if request.method == "POST":
        num = request.POST['number']
        params["number"] = num
        product.in_cart = num
        product.save()

    return render(request, 'ecom/product.html', params)

def pay(request):
    items_in_cart = Item.objects.exclude(in_cart=0)
    total_price = 0
    cart = get_cart()
    for item in items_in_cart:
        total_price += item.in_cart * item.price
    cart.money = total_price
    params = {
        'items':items_in_cart,
        'cart':cart,
    }

    if request.method == 'POST':
        messages.success(request, '決済完了')
        if 'button_2' in request.POST:
            tmp = {}
            for item in items_in_cart:
                tmp[item.product] = item.in_cart
                item.in_cart = 0
                item.save()
                cart.money = 0
                cart.save()
            history = History()
            history.item = tmp
            history.save()

            

    return render(request, 'ecom/pay.html', params)


#----------------

def get_cart():
    cart = Cart.objects.first()
    return cart



