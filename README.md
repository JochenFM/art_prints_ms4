![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# VAP - Vintage Art Prints

Am I responsive

**[Live demo](https://jochenfm-art-prints.herokuapp.com/)**

<span id="top"></span>

## Table of Contents

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-overview">Overview</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#database-model">Database model</a>
- <a href="#features">Features</a>
  - <a href="#features-current">Existing Features</a>
  - <a href="#features-future">Future Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
---


<span id="context"></span>

## Context

VAP - Vintage Art Prints allows trade of and information exchange on a fine selection of original art prints from around the globe. 
The project also publishes blog posts for users to exchange information on the paper art advertised and help an online community of paper art traders and affictionados grow. The current focus is on paper collectibles, so-called “Mono-Karten” or “Monos”, advertising cards developed from around 1905 by Swiss editor and entrepreneur Karl Wilhelm Bührer (1861-1917) under the aegis of International Mono Society, equally founded by Bührer in Winterthur, Switzerland. 
But the product range can be expanded later on with related paper- and artwork, such as other types of vintage advertising cards, poster art, and even stamps.
The Mono cards were designed by then young painters such as Emil Cardinaux, Burkhard Mangold or Ludwig Hohlwein and were collected just as present-day soccer or baseball picture cards. Sized 4x6 inches, the picture side usually contained print art, whereas on the reverse was a brief statement explaining the content of the picture, with carefully crafted advertising slogans of the companies involved in the idea.
I find these cards aesthetically appealing – the beauty of the images, the quality of the colours and of the lithographic printing are amazing. 
What I intend to achieve in this project is to bring together two logics commonly kept apart: for one, an educational/informational logic, following examples such as [Monokartenmatthys](https://www.monokartenmatthys.com/) which allows users to display their cards pointing out their historical and artistic value. For another, a business logic to facilitate trade in these cards and possible profit-making, hitherto often undertaken on [Pinterest](https://www.pinterest.ch/michaelv0271/mono-karten-swiss-trade-cards/) or [Ebay](https://www.ebay.de/itm/384356476574?hash=item597d6e669e:g:3aoAAOSwQ3RhKhtp).


Inspirational for my site were [Galerie 123](https://www.galerie123.com/en/), [King & McGaw](https://www.kingandmcgaw.com/prints/vintage) and [Retrographik](https://retrographik.com/)

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>


<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview

*VAP* addresses everyone who is interested in paper art and its collection and trade for the purpose of profit-making, information exchange and learning, or just for fun and aesthetics. Users are looking for items to purchase securely and trustworthily, while being able to compare market information such as price and product condition. Some would also like to see content to learn from and educate themselves, while potentially also sharing and discussing some of their knowledge on vintage paper collectibles.    
Moreover, the site owner has some specific business goals which include:

* Provide customers with a secure and smooth e-commerce experience
* Make profit from selling products / services
* Establish the shop's brand identity
* Expand the business effectively

All design decisions have been made with the following goals in mind:
- Accessibility
- Ease of use
- Responsiveness
- Visual appeal




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





from the now deleted cart_tool.py template tag ({% load cart_tools %} needs to be added at top of cart.html):
"""from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


    http://hex2rgba.devoth.com/ to get rgba from hex code

Email contact form adjusted from http://reusableforms.com/d/e1/bootstrap-contact-form-send-email

Footer with three-column layout adjusted from https://www.ordinarycoders.com/blog/article/bootstrap-footers 

to check if all tags are closed: https://www.aliciaramirez.com/closing-tags-checker/


From CI Video, "Deploying to Heroku", min 5:41
While I'm here I'll also set debug to be true only if there's a variable called development in the environment.
And now I'll commit these changes and push them to github.

DEBUG = True must change to  DEBUG = 'DEVELOPMENT' in os.environ

def new_arrivals(request):
    """ a view to show new arrivals among products  """

    products = Product.objects.all()

    """template = 'home/new_arrivals.html'"""
    context = {
        'products': products,
        'new_arrivals': new_arrivals,
    }
    return render(request, template, context)


urls.py:     """path('', views.new_arrivals, name='new_arrivals')"""


Footer is inspired by examples from https://www.ordinarycoders.com/blog/article/bootstrap-footers
