from django.shortcuts import (render, redirect, get_object_or_404)
from django.http import HttpResponse
from django.views.generic import (DetailView, View)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Cart
from .forms import CheckoutForm
from POV.settings import EMAIL_HOST_USER
from django.urls import reverse

# Create your views here.
class CartDetailView(DetailView):
    queryset = Cart.objects.all()
    template_name = 'cart/cart_detail.html'

    def get_object(self):
        user = self.request.user
        cart = None
        if user.is_authenticated:
            if Cart.objects.filter(user=user):
                cart = get_object_or_404(Cart, user=user)
                return cart
        return Cart.objects.none()


class CartDeleteView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart.products.clear()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

class ShippingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, './cart/shipping.html', {})
    
    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST or None)
        for i in form:
            print(i)
        if form.is_valid():
            Form_Data = {
                'email': form.cleaned_data['email'],
                'address': form.cleaned_data['address'],
                'specific_details': form.cleaned_data['specific_details'],
            }
            
            # delimeter.
            query_string = '&'.join([f'{key}={value}' for key,value in Form_Data.items()])
            redirect_url = f"{reverse('cart:order')}?{query_string}"
            return redirect(redirect_url)
   
    
class CheckoutView(View):
  
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')
        address = request.GET.get('address')
        specific_details = request.GET.get('specific_details')
        context = {
            'email':email,
            'address': address,
            'specific_details':specific_details,
        }
        
        if request.user.is_authenticated:
            user_cart = Cart.objects.filter(user=request.user)
            if user_cart:
                cart = get_object_or_404(Cart, user=request.user)
                context['cart']=cart
                return render(request, './cart/orderConfirm.html', context=context)
        return render(request, './cart/orderConfirm.html')
        
    
    def post(self, request, *args, **kwargs):
            cart = self.get_cart(request)
            context = self.get_context(request, cart)
            print(context)
            html = render_to_string(
                                        'forms/checkout.html',
                                        context=context
                                    )
            send_mail(
                        subject='Checkout Form Submission',
                        message='Cart',
                        from_email=request.user.email,
                        recipient_list=[EMAIL_HOST_USER],
                        html_message=html
                        )
            return HttpResponse("done")        
            # return redirect(request.META.get('HTTP_REFERER', '/'))

    def get_cart(self, request):
        user = request.user
        return get_object_or_404(Cart, user=user)
    
    def get_context(self, request, cart):
        quantity = request.META.get('QUERY_STRING').split(',')
        context = {
                    'user': cart.user,
                    'quantity': quantity,
                    'products': [],
                    # 'Contact': Form    
                }
        
        counter = 0
        for product in cart.products.all():
            context['products'].append(f'{product.title}: quantity({quantity[counter]})')
            counter += 1
        
        print(context)
        # return context




