from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_cart(request):
    """ a view to return the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """add the specified product to the shopping cart"""
    
    quantity = int(request.POST.get('quantity'))   
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)


