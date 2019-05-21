from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPackage, name='showPackage'),
    path('new', views.newPackage, name='newPackage'),
]