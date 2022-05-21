from dataclasses import fields
from tkinter import Widget

from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
       model = Product
       fields = '__all__'


class ProductImage(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields ='__all__'
