from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth import login


#アカウント情報
class Person(models.Model):
    """Model representing unique user."""
    name = models.TextField()
    #username=request.user.username
    e_mail = models.EmailField()
    password = models.TextField()
    in_cart = models.IntegerField(default=0)
    #cart = models.OneToOneField(Cart,on_delete=models.CASCADE,primary_key=True,)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular user')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

 
    

#商品情報
class Item(models.Model):
    product = models.CharField(max_length=100)
    #pers = models.ManyToManyField(Person)
    picture = models.URLField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    in_cart = models.IntegerField(default=0)
    def __str__(self):
        """String for representing the Model object."""
        return self.product



#購入履歴
class History(models.Model):
    name = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    item = models.CharField(max_length=100)
    


#カートの中身
#class Cart(models.Model):
 #   owner = models.ForeignKey(Person, on_delete=models.SET_NULL,blank=True, null=True)
  #  money = models.IntegerField(default=0)
    
   # def __str__(self):
       # String for representing the Model object.
      # if request.user.is_authenticated:
    #        return self.name
class Cart(models.Model):
    person = models.CharField(max_length=100, default="prakhar")
    money = models.IntegerField(default=0)
    #item=models.ForeignKey(Item,on_delete=models.SET_NULL, null=True)

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular user')
    
    def __str__(self):
       # String for representing the Model object.
      # if request.user.is_authenticated:
            return self.person

    



        
