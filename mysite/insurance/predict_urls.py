from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPredict, name='showPredict'),
]