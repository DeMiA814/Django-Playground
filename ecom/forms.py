from django import forms

class Product_form(forms.Form):
    number = forms.IntegerField(label="number")

class Login_form(forms.Form):
    name = forms.CharField(label="name")
    e_mail = forms.EmailField(label="e_mail")
    password = forms.CharField(label="password")


