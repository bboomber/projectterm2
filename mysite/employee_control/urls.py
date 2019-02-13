from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAllEmp, name='viewAllEmp'),
    path('<str:agent_code>', views.viewEmpDetail, name='viewEmpDetail'),
] 