from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe # new
from ecom.models import Person, Item, History, Cart
from ecom.views import pay
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.utils.decorators import method_decorator
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class PayView(TemplateView):
    template_name = 'payf.html'
    #usernam = .user.username
    #return render('payf.html')

     

    
        
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        usern=Person.objects.filter(name=self.request.user)
        use=usern[0]
        usn=use.name
        car=Cart.objects.get(person=usn)
        #car.money=0
        context= {'key':settings.STRIPE_PUBLISHABLE_KEY,
                   'User':usn,
                  'mon':car.money,
                  'nam':car.person,}
        
        
        return (context)


def charge(request): # new
    
    if request.method == 'POST':
        usn=request.user.username 
        car=Cart.objects.get(person=usn)
       # money=request.session['cart_money']
        #mon=car[0]
        money=car.money
        charge = stripe.Charge.create(
            amount=money,
            currency='jpy',
            description=usn,
            source=request.POST['stripeToken']
        )
        
        item_in_cart = Item.objects.exclude(in_cart=0)
        tmp = {}
        for item in item_in_cart:
                 tmp[item.product] = item.in_cart
                 item.in_cart = 0
                 item.save()
                 
        car.money=0         
        car.save()
        history = History()
        person=Person.objects.get(name=request.user.username)
        history.name=person
        history.item = tmp
        history.save()
        cont={ 'User': usn,
               'mon':car.money,
               'nam':car.person,}
        return render(request, 'charge.html',cont)


    
