from django.urls import path
from . import views

urlpatterns = [
    path('', views.showReport, name='showReport'),
]
