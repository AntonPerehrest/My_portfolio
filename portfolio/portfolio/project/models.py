from django.db import models

class Project(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to='img/')
