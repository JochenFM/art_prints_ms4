from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
posts = [
     {
         'author': 'JochenFM',
         'title': 'Blog Post 1',
         'content': 'First post content',
         'date_posted': 'July 16, 2021',
     }
 ]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)