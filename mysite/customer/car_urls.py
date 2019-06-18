from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllCar, name='showAllCar'),
    path('new/', views.newCar, name='newCar'),
    path('<str:id>/', views.viewCarDetail, name='viewCarDetail'),
]