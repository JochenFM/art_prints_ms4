![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

This project allows trade of and information exchange on niche paper collectibles: so-called “Mono-Karten” or “Monos”, advertising cards developed from around 1905 by Swiss editor and entrepreneur Karl Wilhelm Bührer (1861-1917) under the aegis of International Mono Society, equally founded by Bührer in Winterthur, Switzerland. The cards were designed by then young painters such as Emil Cardinaux, Burkhard Mangold or Ludwig Hohlwein and were collected just as present-day soccer or baseball picture cards. Sized 4x6 inches, the picture side usually contained print art, whereas on the reverse was a brief statement explaining the content of the picture, with carefully crafted advertising slogans of the companies involved in the idea.
I find these cards aesthetically appealing – the beauty of the images, the quality of the colours and of the lithographic printing are amazing. What I intend to achieve in this project is to bring together two logics commonly kept apart: for one, an educational/informational logic, following examples such as https://www.monokartenmatthys.com/ which allows users to display their cards pointing out their historical and artistic value. For another, a business logic to facilitate trade in these cards and possible profit-making, hitherto often undertaken on Pinterest (https://www.pinterest.ch/michaelv0271/mono-karten-swiss-trade-cards/) or ebay.
The product range can be expanded later on with related paper- and artwork, such as other types of vintage advertising cards, poster art, and even stamps.

My site emulates examples such as https://www.galerie123.com/en/, https://www.kingandmcgaw.com/prints/vintage or https://retrographik.com/





<li class="nav-item"><a class="nav-link" href="{% url 'about' %}">About</a></li>
                  <li class="nav-item"><a class="nav-link" href="{% url 'new_arrivals' %}">New Arrivals</a></li>
                  <li class="nav-item"><a class="nav-link" href="{% url 'products' %}">All Products</a></li>
                  <li class="nav-item"><a class="nav-link" href="{% url 'mono_cards' %}">Mono Cards</a></li>
                  <li class="nav-item"><a class="nav-link" href="{% url 'posters' %}">Artistic Posters</a></li>



These are good product grids with bootstrap 4:
https://bbbootstrap.com/snippets/bootstrap-ecommerce-product-grid-view-card-19577966



original in den titel?
nach art deco, Jugendstil suchen fuer images

From https://fonts.google.com/specimen/Old+Standard+TT?query=old+sta:

About Old Standard TT
Old Standard reproduces a specific type of Modern (classicist) style of serif typefaces, very commonly used in various editions of the late 19th and early 20th century, but almost completely abandoned later. However, this lettertype still has at least two advantages:

it can be considered a good choice for typesetting scientific papers, especially on social and humanitarian sciences, as its specific features are closely associated in people's eyes with old books they learned on;
the most beautiful examples of Greek and Cyrillic lettertypes were all based on the classicist style, so for those scripts, "Modern" fonts are much more appropriate than any contemporary (e. g. Times-based) designs.
The name "Old Standard" was selected as opposed to the "Obyknovennaya Novaya" ("New Standard") typeface, widely used in Soviet typography, which represents another, slightly different type of the same Modern style. Of course this name doesn't look very original, but it seems to be a good choice for a revival of the most common lettertype of the early 20th century.



In order to help me create the ERD (=Entity Relationship Diagram):
https://launchschool.com/books/sql/read/table_relationships


slider image from unsplash https://unsplash.com/photos/6NSVToSYwV0

https://imagecolorpicker.com/en



#618BB2 of Pantone colour
#c95939
#dfdcd3
bootstrap bg dark #343a40 Gyunmet

Zoom mouseover for single products: https://www.jquery-az.com/jquery/demo.php?ex=168.0_1

https://www.jquery-az.com/4-demos-to-create-product-galleries-with-zoom-feature-by-jquery/

https://codepen.io/nikki-peel/pen/RwavQer


Do I need to insert new_arrivals into project level urls?
and also into home urls.py?

https://stackoverflow.com/questions/48735726/how-to-get-checkbox-values-in-django-application for get checkbox value in HTML form in django 

From context.py:

"""from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, checked in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count += int(checked)
        cart_items.append({
            'item_id': item_id,
            'checked': checked,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context """

from the now deleted cart_tool.py template tag ({% load cart_tools %} needs to be added at top of cart.html):
"""from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity