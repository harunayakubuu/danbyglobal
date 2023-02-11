from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.contrib import messages


class AboutUs(models.Model):
    about = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.created_date)


class PrivacyPolicy(models.Model):
    # title = models.CharField(max_length = 255)
    policy = RichTextField()
    active = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.created_date)
    
    class Meta:
        verbose_name_plural = "Privacy Policy"


class TermsAndCondition(models.Model):
    # term = models.CharField(max_length = 255)
    terms_and_conditions = RichTextField()
    active = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.created_date)


class Service(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    # picture = models.ImageField(upload_to = "pictures/services")
    description = models.TextField()
    active = models.BooleanField("Active", default = True)
    slug = models.SlugField(max_length = 100, unique = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:service-details', args=[self.slug])