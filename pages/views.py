from django.shortcuts import render, get_object_or_404, redirect
from partners.models import Partner
from projects.models import Project
from accounts.models import Team
from . models import AboutUs, Service
from django.urls import reverse, reverse_lazy


def index(request):
    partners_count = Partner.objects.all().count()
    projects_count = Project.objects.all().count()
    about = AboutUs.objects.all()
    services = Service.objects.all()
    context = {
      'partners_count': partners_count,
      'projects_count': projects_count,
      'about': about,
      'services': services,
    }
    return render(request, 'pages/index.html', context)


def about_us(request):
    about = AboutUs.objects.all()
    partners_count = Partner.objects.all().count()
    projects_count = Project.objects.all().count()
    team = Team.objects.all()
    context = {
      'about': about,
      'team': team,
      'partners_count': partners_count,
      'projects_count': projects_count,

    }
    return render(request, 'pages/about-us.html', context)


def team(request):
    team = Team.objects.all()
    context = {
      'team': team
    }
    return render(request, 'pages/team.html', context)


def team_member_details(request, id):
    member = get_object_or_404(Team, id = id)
    context = {
      'member': member
    }
    return render(request, 'pages/team-member-details.html', context)

def privacy_policy(request):
    
    context = {

    }
    return render(request, 'pages/privacy_policy.html', context)


def terms_and_conditions(request):
    
    context = {

    }
    return render(request, 'pages/terms_and_conditions.html', context)


def services(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'services/services.html', context)


def service_details(request, slug):
    service = get_object_or_404(Service, slug = slug)
    context = {
        'service':service
    }
    return render(request, 'services/service-details.html', context)