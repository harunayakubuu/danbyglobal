from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    logo = models.ImageField(upload_to = 'pictures/partners')
    website = models.URLField(blank = True, null = True)
    active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'