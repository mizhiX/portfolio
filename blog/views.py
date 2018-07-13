from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def blog(requrest):
    blog = Blog.objects
    return render(requrest, 'blog.html', {'blogs': blog})