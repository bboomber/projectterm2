from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllCus, name='showAllCus'),
    path('new/', views.newCus, name='newCus'),
    path('<str:id>/', views.viewCusDetail, name='viewCusDetail'),
]