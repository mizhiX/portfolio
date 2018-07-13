from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(default='文章标题' ,max_length=50)
    date = models.DateField()
    img = models.ImageField(default='images/error_1.png', upload_to='images/')
    text = models.TextField(default='正文')