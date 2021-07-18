from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    """category = models.CharField(max_length=254)
    updated_on = models.DateTimeField(auto_now=True)"""

    def __str__(self):
        return self.title

    
    """def __str__(self):
        return '{}, {}'.format(self.title,
                               self.category)"""


