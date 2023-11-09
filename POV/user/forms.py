from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs = {
                                                'placeholder': 'Enter Your Email'
                                            }
        self.fields['password1'].widget.attrs = {
                                                'placeholder': 'Enter Your Password'
                                            }
        self.fields['password2'].widget.attrs = {
                                                'placeholder': 'Re-Type Password'
                                            }

    class Meta:

        model = User
        fields = [
                    'email'
                 ]
        

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(
                                                        attrs={
                                                                'placeholder': 'Enter Your Email'
                                                              }
                                                   )
                            )
    password = forms.CharField(widget=forms.PasswordInput(
                                                            attrs={
                                                                    'placeholder': 'Enter Your Password'
                                                                  }
                                                         )
                              )


