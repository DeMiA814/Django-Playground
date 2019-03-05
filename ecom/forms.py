from django import forms

class Product_form(forms.Form):
    CHOICE = (
    ('0', '数量を選択'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    )
    number = forms.ChoiceField(label="本数",widget=forms.Select, choices=CHOICE)

class Login_form(forms.Form):
    name = forms.CharField(label="name")
    e_mail = forms.EmailField(label="e_mail")
    password = forms.CharField(label="password")


