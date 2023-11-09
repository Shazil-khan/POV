from .forms import CheckoutForm

def get_checkout_form(request):

    # form = CheckoutForm(initial={'email':request.user.email})
    return {
                'checkout_form': CheckoutForm()
           }
    
