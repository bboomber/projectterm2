from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAllEmp, name='viewAllEmp'),
    path('new', views.get_name, name='get_name'),
    path('<str:agent_code>/', views.viewEmpDetail, name='viewEmpDetail'),
] 