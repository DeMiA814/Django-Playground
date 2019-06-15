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
        context= {'key':settings.STRIPE_PUBLISHABLE_KEY,
                   'User':usn,}
        
        
        return (context)


def charge(request): # new
    
    if request.method == 'POST':
        
        #token = request.session['token'] 
        money = request.session['cart_money']          
        charge = stripe.Charge.create(
            amount=money,
            currency='jpy',
            description='Demion',
            source=request.POST['stripeToken']
        )
        usn=request.user.username
        cont={ 'User': usn
               }
        return render(request, 'charge.html',cont)


    
