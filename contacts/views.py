from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit = False)
            form_instance.save()
            messages.success(request, "We've received your message. We shall get back to you shortly.")
            
            send_mail(
                subject = "Contact Form Message.",
                message = "You have just been sent a message via the website Kindly log in to read and update the message status",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = ['danbyglobal@gmail.com']
            )

            return redirect('contacts:contact-form')
    context = {
        'form': form,
    }
    return render(request, 'contacts/contact-form.html', context)