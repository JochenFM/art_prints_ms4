from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ a view to return the cart contents page """
    return render(request, 'cart/cart.html')


def  add_to_cart(request, item_id):
    """add the specified product to the shopping cart"""
    
    checked = request.POST.get('checked')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = checked

    request.session['cart'] = cart
    return redirect(redirect_url)
