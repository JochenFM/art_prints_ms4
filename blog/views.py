from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.


def blog(request):
    return render(request, 'blog/blog.html')