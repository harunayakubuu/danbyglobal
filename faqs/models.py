from django.db import models
from django.utils.text import slugify


class Faq(models.Model):
    question    = models.CharField(max_length = 255)
    answer      = models.TextField()
    active      = models.BooleanField('Active', default = False)
    slug        = models.SlugField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.question

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        return super(Faq, self).save(*args, **kwargs)