from django.db import models

# Create your models here.

class Gallery(models.Model):
    intro = models.CharField(max_length=100)