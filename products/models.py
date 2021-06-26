from django.db import models


class Category(models.Model):
    # this name should be readable in other code, can be mono_cards

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=True)
    # friendly name is for front end, can be Mono Cards
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string method to return category model
    def __str__(self):
        return self.name

    # model method to return the friendly name if needed
    def get_friendly_name(self):
        return self.friendly_name


# product model


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)

    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.DecimalField(max_digits=1, decimal_places=0, null=True, 
                                    blank=True)
    dimension = models.CharField(max_length=40, null=True, blank=True)
    year = models.DecimalField(max_digits=6, decimal_places=0, null=True, 
                               blank=True)                           
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
   
