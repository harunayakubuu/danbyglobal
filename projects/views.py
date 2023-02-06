from django.shortcuts import render, get_object_or_404
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'projects/projects.html', context)


def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        'project':project
    }
    return render(request, 'projects/project-details.html', context)
