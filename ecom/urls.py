
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views as ecom_views
from django.views.generic.base import TemplateView # new

urlpatterns = [
    #path('',views.login, name="login"),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    #path('login',views.login, name="login"),
    path('product.html', views.product, name="product"),
    path('', include('django.contrib.auth.urls')),
    url('signup', ecom_views.signup, name='signup'),
    path('pay.html', views.pay, name="pay"),
    path('history.html', views.history, name="history"),
    path('cancel/<product>', views.cancel, name='cancel')
    #path('pay1.html', TemplateView.as_view(template_name='pay1.html'), name='pay1'),
]
