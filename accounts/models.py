from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)

    # USER_ROLES = (
    #     ('CHAIRMAN', 'Chairman'),
    #     ('MD', 'Managing Director'),
    #     ('DAHR', 'Director Admin and Human Resource'),
    #
    # )
    # role = models.CharField(max_length=50, choices = USER_ROLES, default = 'CUSTOMER')

    
    def get_full_name(self):
        #Return the first_name plus the last_name, with a space in between.
        if self.middle_name:
            full_name = '%s %s %s' %(self.first_name, self.last_name, self.middle_name)
        else:
            full_name = '%s %s' %(self.first_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        #Return the short name for the user.
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = "pictures/profile_pictures", blank = True, null = True)
    additional_phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        
post_save.connect(post_user_created_signal, sender=Account)


class Team(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    DESIGNATION_CHOICES = (
        ('DAW', 'Director Admin and Warehouse'),
        ('OMM', 'Operational and Marketing Manager'),
        ('DFL', 'Director Finance and Logistics'),
    )
    designation = models.CharField(max_length = 20, choices = DESIGNATION_CHOICES)
    words = models.CharField(max_length = 100)
    about = models.TextField()
    display_picture = models.ImageField(upload_to = 'pictures/team/')
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.user.email}'