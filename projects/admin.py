from django.contrib import admin
from . models import Project, ProjectPicture


class ProjectPictureInline(admin.TabularInline):
    model = ProjectPicture
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectPictureInline,
    ]
    list_display = ['name', 'start_date', 'finish_date', 'complete']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Project, ProjectAdmin)