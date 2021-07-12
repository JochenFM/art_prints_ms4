from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):
    """ a view to return the index page """
    return render(request, 'home/index.html')


def new_arrivals(request):
    """ a view to show new arrivals among products  """

    products = Product.objects.all()

    template = 'index.html/new_arrivals'
    context = {
        'products': products,
        'new_arrivals': new_arrivals,
    }
    return render(request, template, context)

