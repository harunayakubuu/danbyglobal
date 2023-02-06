from django.contrib import admin
from .models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
admin.site.register(Partner, PartnerAdmin)