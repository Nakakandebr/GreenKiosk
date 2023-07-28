from django import forms
from .models import  Product_Cart

class Product_CartGetForm(forms.ModelForm):
    class Meta:
        model =  Product_Cart
        fields = "__all__"

