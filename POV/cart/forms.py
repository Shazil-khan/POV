from django import forms
from .models import Cart


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField()
    product = forms.CharField(widget=forms.Textarea())

    class Meta:

        model = Cart
        fields = [
                  'quantity',
                  'product'
                 ]
        

class CheckoutForm(forms.Form):
    email = forms.EmailField(max_length=100, 
                             widget=forms.TextInput(
                                                        attrs={
                                                                'placeholder': 'Enter Your Email',
                                                                'class': 'form-control form-items'
                                                                 
                                                              }
                                                   )
                            )
    address = forms.CharField(max_length=255,
                              widget=forms.TextInput(
                                                        attrs={
                                                                'placeholder': 'Enter Your Address',
                                                                'class': 'form-control form-items'
                                                              }
                                                    )
                             )
    specific_details = forms.CharField(widget=forms.Textarea(
                                                                attrs={
                                                                        'placeholder': 'Enter Specific Details',
                                                                        'class': 'form-control form-items'

                                                                      }
                                                            ), 
                                       required=False
                                      )