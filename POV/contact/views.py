from django.shortcuts import (render, get_object_or_404, redirect)
from django.views.generic import View
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
from POV.settings import EMAIL_HOST_USER

# Create your views here.

class ContactFormView(View):

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            context = {
                        'Subject': 'Contact From Submission',
                        'name': name,
                        'Email': email,
                        'message': msg 
                    }
            html = render_to_string(
                                    'forms/contact.html', 
                                    context=context
                                )
            send_mail(
                        subject='Contact From Submission',
                        message='Hello World',
                        from_email=request.user.email,
                        recipient_list=[EMAIL_HOST_USER],
                        html_message=html
                    )
            return redirect(request.META.get('HTTP_REFERER', '/'))