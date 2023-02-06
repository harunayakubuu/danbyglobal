from django.urls import path
from .views import contact_form


app_name = "contacts"


urlpatterns = [
    path('contact-form/', contact_form, name = 'contact_form')
]