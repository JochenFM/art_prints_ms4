from django.shortcuts import render
from .models import Product, Category


def index(request):
    """ a view to return the index page and display products of
    new_arrivals category """
    
    
    products = Product.objects.all().filter(category__name__in=new_arrivals)
    print("filter products", products)
    
    return render(request, 'home/index.html', context)

