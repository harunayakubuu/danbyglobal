from django.shortcuts import render
from .models import Faq
from django.core.paginator import Paginator


def faqs(request):
    faqs = Faq.objects.order_by('-created_at').filter(active = True)
    paginator = Paginator(faqs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'faqs/faqs.html', context)