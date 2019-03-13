from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllInsure, name='showAllInsure'),
    path('sell', views.sellInsure, name='sellInsure'),
]