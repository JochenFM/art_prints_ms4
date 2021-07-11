from django.shortcuts import render

# Create your views here.


def profiles(request):
    """to display user's profile"""
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)