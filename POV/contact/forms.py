from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100, 
                           widget=forms.TextInput(
                                                    attrs={
                                                            'placeholder': 'Enter Your Name',
                                                            'class': 'contactForm'
                                                          }
                                                 )
                          )
    email = forms.EmailField(
                                widget=forms.TextInput(
                                                        attrs={
                                                                'placeholder': 'Enter Your Email',
                                                                'class': 'contactForm'
                                                                }
                                                      )
                            )
    message = forms.CharField(widget=forms.Textarea(
                                                        attrs={
                                                                'placeholder': 'Your Message Here',
                                                                'class': 'contactForm'

                                                              }
                                                   )
                             )