from django import forms
from .models import (Product, Category)


class ProductForm(forms.ModelForm):

    title = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(
                                        queryset=Category.objects.all()
                                     )
    price = forms.IntegerField()
    instock_qty = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea())
    custom = forms.BooleanField()

    class Meta:

        model = Product
        fields = [
                    'title', 
                    'category', 
                    'price', 
                    'instock_Qty', 
                    'description', 
                    'custom'
                 ]