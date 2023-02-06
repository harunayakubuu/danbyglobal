from django.shortcuts import render
from .models import Partner


def partners(request):
    partners = Partner.objects.all()
    context = {
        'partners':partners
    }
    return render(request, 'partners/partners.html', context)