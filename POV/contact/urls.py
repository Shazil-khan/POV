from django.urls import (path, include)
from .views import ContactFormView

app_name = 'contact'

urlpatterns = [
    path('', ContactFormView.as_view(), name='mail')
]
