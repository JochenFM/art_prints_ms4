from django.shortcuts import render
from products.models import Product, Category


def index(request):
    """ a view to return the index page and display products of
    new_arrivals category """
    
    products = Product.objects.filter(category__name="new_arrivals")
    
    context = {
        'products': products,
       
    }
    return render(request, 'home/index.html', context)

