from django.urls import path
from .views import partners


app_name = "partners"


urlpatterns = [
    path('', partners, name = 'partners')
]