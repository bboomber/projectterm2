from django.urls import path
from . import views

urlpatterns = [
    path('', views.remind, name='remind'),
    path('1', views.remind, name='remind'),
    path('2', views.remind2, name='remind2'),
    path('3', views.remind3, name='remind3'),
    path('4', views.remind4, name='remind4'),
    path('5', views.remind5, name='remind5'),
    path('6', views.remind6, name='remind6'),
    path('7', views.remind7, name='remind7'),
    path('8', views.remind8, name='remind8'),
    path('9', views.remind9, name='remind9'),
    path('10', views.remind10, name='remind10'),
    path('11', views.remind11, name='remind11'),
    path('12', views.remind12, name='remind12'),
] 