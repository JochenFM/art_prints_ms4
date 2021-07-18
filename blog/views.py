from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)