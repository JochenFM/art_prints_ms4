from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request, new_arrivals):
    """ a view to return the index page and display products of
    new_arrivals category """

    category = get_object_or_404(Category, new_arrivals=new_arrivals)
    products = category.products.all()
    context = {
        'title': category.name,
        'products': products,
    }
    
    return render(request, 'home/index.html', context)



  
