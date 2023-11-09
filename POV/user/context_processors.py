from .forms import (LoginForm, SignUpForm)

def get_user_forms(request):

    return {
                'signup_form': SignUpForm(),
                'login_form': LoginForm()
           }