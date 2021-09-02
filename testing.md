<span id="top"></span>

Back to [README](README.md)

## Index

- <a href="#testing-manual">Manual Testing</a>
- <a href="#testing-auto">Automated Testing</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved issues</a>
- <a href="#testing-unresolved">Unresolved issues</a>

---

<span id="testing-manual"></span>

## Manual testing

The following tests have been carried out without issue. While reporting them, I will also come back to some of the user stories mentioned in [README.md](https://github.com/JochenFM/art_prints_ms4/blob/master/README.md) to see how the requirements have been met:

### Landing Page
#### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | See at a glance what services are offered | Find the service I want to use (US002) |
### Test conducted:
- Click all the buttons and links on the page
- Submit contact Form to see if the admin receives an email
### Result:
- All the buttons and links are working as expected. 
- Contact form at the bottom of the page is not functional. Requires development at a later stage. 


### Navbar
#### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- | 
| Shopper | All the important services are accesible from nav bar| Don't need to scroll to find important information (US003)|
### Test conducted:
- All links in the navbar direct to the correct pages.
- On screen widths greater than 991px:
The correct menu options appear depending on the user's session status:
  - **Not logged in**: Brand Title, Online Shop, Blog, My Account with Log In and Register, Cart 
  - **Logged in**: Brand Title, Online Shop, Blog, My Account with My Profile, New Post, and Logout, Cart
  - **Logged in as superuser**: Brand Title, Online Shop, Blog, My Account with with Product Management, My Profile, New Post, and Logout, Cart
- Tapping/clicking each link takes the user to the relevant page, or logs the user out.
- Clicking on Navbar brandlogo takes user back to index page.


Smaller than 991px:
 
- The available menu options are replaced by a hamburger icon.
- All available menu options appear in a drop down nav when the hamburger icon is tapped/clicked, including the search bar. 
- VAP Brand title in Navbar and hamburger menu icon swap sides.



### Onlineshop
#### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Search a product with keywords | Find the most appropriate products (US015)|
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing (US016)|
| Shopper | Filter by a specific category | Easily find products in a specific category (US017)|
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular with other customers (US018)|
| Site Owner | Easily add a new product | Make sure the online site has the latest catalogue (US019)|
### Test conducted:
- Inserted various keywords in search bar and check if it works as expected.
- Checked if the online shop page / the individual product page is displayed without breaking the layout for common screensizes.
- Navigations such as paginations, back to previous page button etc. don't break 
- Checked that the sorting by the given categories and the filtering by prize, name etc. all work fine
### Result:
- Button layout needed various style fixes to follow responsiveness and the secure checkout button in the cart still does re-size awkwardly 
- Dropdown menus for categories and search by on onlineshop still sit awkwardly and the dropdown menu gets in the way of good visuality. Therefore, most issues on the product cards have been fixed, notwithstanding the minor jumble-up of style of date is "N/A". 
- Product edit and delete all work fine including the pop up messages warning the site owner of the course of action.

#### Cart, Purchasing and Checkout
#### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily select a product and know about the condition it is in | Ensure I purchase the correct product and am not surprised at its condition (US024)| 
| Shopper | Easily add a product to my cart and see what is in my cart | Select the right product and double-check whether this is true (US025)| 
| Shopper | Easily remove a product from my cart | Delete a wrongly selected product and proceed only with what I intend to buy (US026)| 
| Shopper | store my shipping details |Check out easier next time I visit that page (US027)|

### Tests conducted:
- Condition the mono cards are in is indicated but at the moment there is no appropriate legend telling users what it means.
- Adding and removing to/from cart, also adding the same product multiple times
- Check if Remove/Edit links work properly.
### Result:
- Mixed result in this case as the information for the Condition is failry important
- At the moment, the same product can be added multiple times which is illogic for an art gallery of collectibles and unique items.
- Also, removing a product from the cart does not trigger a toast message that is has been successfully removed
- Remove/Edit links work as expected.


### Blog
#### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Post a blog about the paper products or related collectibles | Provide shoppers or interested users with interesting information about the paper collectibles (US013)|
| Shopper/site user | Filter blog posts by specific categories | See at a glance whether information is available about a topic I am interested in (US023)|
| Site owner | Easily add, update, or delete blog posts  | Make sure that the blog posts are up-to-date and to remove potentially harmful content (US029)|
#### Tests conducted:
- Click all the links in this section: links to each post, the links to individual augthors, and the delete/edit buttons for registered post authors. That includes the pagination links and their peculair logic
- The responsiveness of the box elements, pagination links included 
### Result:
- All links work fine, including edit and delete posts.
- Main issue here apart from lack of visual appeal is that the site owner cannot yet delete/edit posts but only an author for his/her own posts. This would make it impossible to remove false or harmful content and therefor needs to be addressed.   
- Pagination button's Overlap beyond the box elements of individual blog posts has been resolved by adding justify-content-center but as box elements are not placed in the middle this resultsn in a slightly skewed layou at the moment. 

### Footer

Additionally, it should be reported that after much trying with justify-content and responsiveness, the footer has a simple three-column layout and 'sticks' on the bottom of the screen with only basic content, inlcuding the brand logo.
- Below 991px, it responsively turns to one column.
- Each social media link opens the relevant external page in a new window.


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>


<span id="testing-auto"></span>

## Automated testing


[W3C - CSS](https://jigsaw.w3.org/css-validator/) returned:

![CSS Validator](readme_materials/css_validation.png)


In response to the [W3C - HTML](https://validator.w3.org/) errors shown:

- I removed a number of stray div tags and closed missing tags for div, p, span, button and form elements.
- I deleted wrong or unnecessary labels, roles and types for form and scripts elements.

I left the "Warning: The type attribute is unnecessary for JavaScript resources." as it is.


[CSS Lint](http://csslint.net/) - 0 errors, 47 warnings - **PASS**

- I removed unit specification behind 0 values
- In one instance warning was for "overqualified elements" - the fontawesome shopping cart icon in the navbar, for which I removed the i element accordingly.
- many warnings refer to "Require compatible vendor prefixes" or "Disallow duplicate properties" both of which were added by autoprefixer and left untouched by me.
- Others discourage the use of id for selectors or adjoining classes ("Don't use IDs in selectors", "Don't use adjoining classes.") Selecting via IDs, however, 
has only been used for styles which will not be reused and the specificity was needed.


- LightHouse on Google DevTool
Lighthouse tests were conducted on the Landing Page, Online Shop Page/Single Product Page, Blog Page, Cart Page.

Results for Performance, Accessibility, Best Practices, and SEO were all in the region between 68% and 100%.

In light of the Lighhouse Reports, improvements at a later stage need to be implemented on:

- Performance on landing page which currently is at 81% due to:
  - Image in PNG format which could be replaced with that of WebP and AVIF which often "provide better compression than PNG or JPEG, which means faster downloads and less data consumption."
  - Render-blocking resources such as critical JS/CSS which could go inline in the future.

- Performance on online-shop for pretty much the same reasons as in the previous point with the addition that Lighthouse suggested to properly size the images "to save cellular data and improve load time."

- Accessibility on the onlineshop page is currently at 85% due to
  - social media links in the footer having an `[aria-hidden="true"]` element which "prevent those interactive elements from being available to users of assistive technologies like screen readers." As I did not see the element, issue was left unchanged for now.
  - The blue Edit element on the cards apparently does not have "sufficient contrast ratio" between background and foreground colors.

- Performance of the product_detail page was hampered by the fact that "image elements do not have explicit width and height" which definitely needs to be addressed at a later stage by following these [web.dev ideas](https://web.dev/optimize-cls/?utm_source=lighthouse&utm_medium=devtools#images-without-dimensions).

Performance on the Cart page is currently at 83% due to "render-blocking resources" and, again, unappropriately sized images.

Blog pages are simple enough and scored between 90% and 97% in all Lighhhouse criteria. 



<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-responsive"></span>

## Responsiveness


The site is supported by [Bootstrap](https://getbootstrap.com/) and has been thoroughly tested at all stages of development using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).
Bootstrap may limit design choices and customization at times, but this was an acceptable compromise given the advantages provided, such as a fluid responsive grid system which was used throughout this site, including the container class and a number of Components, such as buttons, Contents, such as tables, and Utilities (Display, Position etc.) 



<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

### Browsers

Tested on:

- Chrome
- Edge
- Firefox
- Safari (iOS)


### Screen sizes

Tested with Chrome DevTools using profiles for:


- Galaxy S5
- Pixel 2
- iPhone 5 SE
- iPhone 6/7/8
- iPhone X
- iPad Pro

I also used the responsive profiles of:

- Mobile M (375px)
- Mobile L (425px)
- Tablet (768px)
- Laptop (1024px)
- Laptop L (1440px)

Real world testing on:

- iPad Air 
- iPhone 11
- MacBook Air
- ASUS VivoBook 14/15
- Huawei P Smartphone  


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>



## Issues and bugs

<span id="testing-resolved"></span>

### Resolved

**One of the key issues on the landing page was to inject a selection of products of the new_arrivals category into the template. The issue failed as long as I had not realized that on a one-page webiste, rendering has to be done to the same site, i.e. index.html. Furthermore, grabbing the right projects from the databasew failed until Sheryl and Michael tutored me and suggested I grab them by the Django lookup method filter them.**

As the error message "Cannot resolve keyword 'category_name' into field.", I used a field look up like category__name to query the Product model as the product and category models are related with a foreign key. I've been reading in django docs about these field lookups and using __in is done when there is a list. So given the category model defines itself using self.name, category__name="new_arrivals" did work.

The function now looks as follows and works with the forloop in the template: {% for product in products %}


def index(request):
    """ a view to return the index page and display products of
    new_arrivals category """
    
    products = Product.objects.filter(category__name="new_arrivals")
    
    context = {
        'products': products,
       
    }
    return render(request, 'home/index.html', context)


The If-statement  {% if product.category.name == 'new_arrivals' %}I had originally inserted, is not needed as I am already filtering the products in the view.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-unresolved"></span>


### Unresolved

**In terms of styling, the text-over-image in the overlayed hero image in its current state is still only a second-best solution even although markedly improved from how it was before.**  

I have gone through a number of options, such as [overlays](
https://stackoverflow.com/questions/30113116/overlaying-an-image-with-text-in-materialize-css), text-over-image [hacks](
https://www.slideteam.net/blog/11-hacks-to-make-text-over-images-more-readable-craft-a-stunning-slide), and related [css-tricks](https://css-tricks.com/design-considerations-text-images/), but so far they have proven stylistically unappealing.   
