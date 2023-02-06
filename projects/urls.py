from django.urls import path
from . views import projects, project_details


app_name = 'projects'


urlpatterns = [
    path('', projects, name = 'projects'),
    path('project/<int:id>/', project_details, name = 'project-details'),
]