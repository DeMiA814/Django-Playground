from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse

from .models import Person, Item, History, Cart
from .forms import Product_form

from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


import stripe
from ecom.models import *
from django.conf import settings
import stripe

# Create your views here.

from django.views.generic.base import TemplateView

from .models import History

import json

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    products = Item.objects.all()
    params = {
        'products':products,
    }
    if request.user.is_authenticated:

        return render(request, 'ecom/index1.html', params)
    else:
        pay.items_in_cart=0
        return render(request, 'ecom/indexlo.html', params)




"""def login(request):
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
"""
def product(request):

   if (request.user.is_authenticated):
        cart = get_cart(request)
        number = 0
        buy_num = 0
        product_name = request.GET.get('product')
        product = Item.objects.get(product=product_name)
        cart.item = product
        print("check")

        if request.method == 'POST':
            print("check2")
            num = request.POST['number']
            buy_num = request.POST['number']
            product.in_cart = num
            cart = get_cart(request)
            tot=int(product.in_cart)*int(product.price)
            cart.money=cart.money+tot
            cart.save()
            item_in_cart = Item.objects.exclude(in_cart=0)
            #total_price=0
            #for item in item_in_cart:
            #   total_price = item.in_cart * item.price
            #  cart.money += total_price
            # cart.save()
            product.save()

        params = {
            'product':product,
            'form':Product_form(),
            # 'number':num,
            'cart':cart,
            'buy_num':buy_num,
            }


        return render(request, 'ecom/product.html', params)
   else:
      # messages.add_message(request, messages.INFO, 'login to proceed')
       return render(request, 'ecom/pay1.html')

def pay(request):
    if request.user.is_authenticated:
        username = request.user.username
        person = Person.objects.get(name=username)
        cart = get_cart(request)
        #item_in_cart = Item.objects.exclude(in_cart=0)
        item_in_cart = Item.objects.exclude(in_cart=0)
        #total_price = 0
        #for item in item_in_cart:
         #   total_price += item.in_cart * item.price
        #cart.money = total_price
        #cart.save()


        params = {
            'items':item_in_cart,
            'cart':cart,
        }

        '''if (request.method == 'POST' ):

            tmp = {}
            for item in item_in_cart:
                tmp[item.product] = item.in_cart
                item.in_cart = 0
                item.save()
                #cart.item.in_cart=0
                #cart.item={}


            cart.money = 0
            cart.save()
            history = History()
            person=Person.objects.get(name=request.user.username)
            history.name=person
            history.item = tmp

            #for history in History:
            history.save()

           # messages.success(request, '決済完了')
            return redirect(to='/ecom/pay.html')
            '''
        return render(request, 'ecom/pay.html',params)
    else:
            #messages.add_message(request, messages.INFO, 'Please login to buy form us.')
        return render(request, 'ecom/pay1.html')

def cancel(request, product):
    if request.user.is_authenticated:
        username = request.user.username
        person = Person.objects.get(name=username)
        cart = get_cart(request)
        #item_in_cart = Item.objects.exclude(in_cart=0)
        item = Item.objects.get(product=product)
        item.in_cart = 0
        item.save()
        return redirect('pay')

#----------------

def get_cart(request):
    #username = None
    if request.user.is_authenticated:
        username = request.user.username
        cart = Cart.objects.get_or_create(person=username)
        print(cart)
        #cart = Cart(request,00)

        return cart[0]

def history(request):
    person = Person.objects.get(name=request.user)
    data = History.objects.filter(name=person)

    params = {
        'data':data,
    }
    return render(request, 'ecom/history.html', params)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print('ok')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            person=Person.objects.create(name=username,password=raw_password,e_mail="abc@ddd.com")
            person.save()
            cart=Cart.objects.create(person=username)
            cart.save()
            #username = request.username['username']
            #password = request.raw_password['password1']
            #user = authenticate(username=username, password=raw_password)
           # p=Person.objects.first()
           # p.save(force_insert=True)
            #model.Person.username= (username=username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
