from django.db import models


#アカウント情報
class Person(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)



#商品情報
class Item(models.Model):
    product = models.CharField(max_length=100)
    picture = models.URLField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    in_cart = models.IntegerField(default=0)



#購入履歴
class History(models.Model):
    name = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    item = models.CharField(max_length=100)


#カートの中身
class Cart(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL,blank=True, null=True)
    money = models.IntegerField(default=0)


