from django.db import models

# Create your models here.

class Gallery(models.Model):
    intro = models.CharField(default='描述', max_length=100)
    img = models.ImageField(default='images/error_1.png', upload_to='images/')
    title = models.CharField(default='标题', max_length=50)
    def __str__(self):
        return  self.title