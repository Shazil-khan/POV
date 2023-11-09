from .forms import ContactForm

def get_contact_form(request):

    return {
                'contact_form': ContactForm()
           }