
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='new_arrivals')
]
