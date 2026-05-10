from django import forms
from .models import Product
from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','quantity','description','reorder_level']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','quantity']

