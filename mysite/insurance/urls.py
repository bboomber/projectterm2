from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllInsure, name='showAllInsure'),
    path('emp', views.showEmpInsure, name="showEmpInsure"),
    path('sell', views.sellInsure, name='sellInsure'),
    path('sellNew', views.newCusSell, name='newCusSell'),
    path('<str:id>', views.viewInsureDetail, name='viewInsureDetail'),
]