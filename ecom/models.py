from django.db import models
from django.conf import settings
from django.utils import timezone


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
 
    def __str__(self):
        return self.product


#購入履歴
class History(models.Model):
    item = models.ForeignKey(Item, verbose_name='購入', on_delete=models.PROTECT)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.PROTECT)
    is_sended = models.BooleanField('発送', default=False)
    stripe_id = models.CharField('タイトル', max_length=200)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{} {} {}'.format(self.item, self.user.email, self.is_sended)


#カートの中身
class Cart(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL,blank=True, null=True)
    money = models.IntegerField(default=0)


