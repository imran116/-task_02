from django.db import models

# Create your models here.
class Management(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='management/')

    def __str__(self):
        return self. title

class ManagementFeature(models.Model):
    icon = models.ImageField(upload_to='icons/')
    project_name = models.CharField(max_length=30)
    total_project_number = models.IntegerField()
    project_description = models.TextField(max_length=300)

    def __str__(self):
        return self.project_name