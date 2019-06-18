from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAllEmp, name='viewAllEmp'),
    path('<str:id>/', views.viewEmpDetail, name='viewEmpDetail'),
    path('<str:id>/edit', views.editEmp, name='editEmp'),
] 