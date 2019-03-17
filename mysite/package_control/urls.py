from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPackage, name='showPackage'),
    path('add', views.addPromotion, name='addPromotion'),
]