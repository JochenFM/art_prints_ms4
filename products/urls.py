from django.urls import path
from . import views


urlpatterns = [
    path('', views.onlineshop, name='onlineshop'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
