
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.new_arrivals, name='new_arrivals')
]
