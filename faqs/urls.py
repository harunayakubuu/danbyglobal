from django.urls import path
from .views import faqs


app_name = "faqs"


urlpatterns = [
    path('', faqs, name = 'faqs')
]