from django.urls import path
from . import views

urlpatterns = [
    path('car', views.newCar, name='newCar'),
    path('customer', views.newCus, name='newCus'),
]