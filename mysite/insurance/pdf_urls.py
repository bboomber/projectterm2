from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>', views.turnToPDF, name='trunToPDF'),
]