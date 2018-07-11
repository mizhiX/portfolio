from django.contrib import admin

# Register your models here.
from gallery.models import Gallery
# 注册models里的Gallery类
admin.site.register(Gallery)