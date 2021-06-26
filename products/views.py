from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def onlineshop(request):
    """ a view to show all products in online shop  """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products_onlineshop.html', context)


def product_detail(request, product_id):
    """ a view to show a single product in detail  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)