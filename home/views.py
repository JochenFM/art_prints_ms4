from django.shortcuts import render
from .models import Product, Category


def index(request):
    """ a view to return the index page and display products of
    new_arrivals category """
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'home/index.html', context)
