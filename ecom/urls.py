from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.login, name="login"),
    path('product.html', views.product, name="product"),
    path('pay.html', views.pay, name="pay"),
]

