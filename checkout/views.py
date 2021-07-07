from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect(reverse('onlineshop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JAe6BAAEx1K6q8frbEF4UPqbrPHcBibglGKzTxSBo3mUNg8jygjLQ6H3mPOfzDDCe7bigSzlEnW3A2ne5IdG9oK00om7W5mqF',
        'client_secret': 'test client secret'  
    }

    return render(request, template, context)
