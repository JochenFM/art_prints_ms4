from django.shortcuts import render
from .models import Product

# Create your views here.


def onlineshop(request):
    """ a view to show all products in online shop  """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products_onlineshop.html', context)
