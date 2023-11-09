from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import (render, redirect)
from django.contrib.auth import (authenticate, login, logout)
from django.views.generic import (CreateView, View)
from django.contrib.auth.models import User
from .forms import (SignUpForm, LoginForm)
from cart.models import Cart

# Create your views here.

class SignUpView(CreateView):

    queryset = User.objects.all()
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User(username=email, email=email)
            user.set_password(password)
            user.save()
            user = authenticate(username=email, password=password)
            if user:
                Cart.objects.create(user=user)
                login(self.request, user)
            return redirect(self.request.META.get('HTTP_REFERER', '/'))
        

class LoginView(View):

    def get(self, request, *args, **kwargs):
    
        form = LoginForm(request.POST or None)
        return render(request, 'registration/login.html', {'form':form})

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                if not Cart.objects.filter(user=user).exists():
                    Cart.objects.create(user=user)
                login(request, user)
                return redirect(request.META.get('HTTP_REFERER', '/'))
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('../products/list')

