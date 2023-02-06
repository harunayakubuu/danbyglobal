from django.urls import path
from .views import (
    index, about_us, privacy_policy, 
    terms_and_conditions, team_member_details, 
    team, services, service_details
)


app_name = "pages"


urlpatterns = [
    path('', index, name = 'index'),
    path('about-us/', about_us, name = 'about_us'),
    path('terms-and-conditions/', terms_and_conditions, name = 'terms_and_conditions'),
    path('privacy-policy/', privacy_policy, name = 'privacy_policy'),
    path('our-team/', team, name = 'team'),
    path('team/member/<int:id>/', team_member_details, name = 'team_member_details'),
    path('services/', services, name = 'services'),
    path('services/<int:id>/', service_details, name = 'service_details'),
]