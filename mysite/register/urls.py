from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('completed', views.saveData, name='completed'),
] 