from django.db import models


class Project(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField(blank = True, null = True)
    complete = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 50, unique = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectPicture(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to = "pictures/projects")
    
    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = 'Project Picture'
        verbose_name_plural = 'Project Pictures'