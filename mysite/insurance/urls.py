from django.urls import path, include
from . import views
from .views import GeneratePDF

urlpatterns = [
    path('', views.showAllInsure, name='showAllInsure'),
    path('emp', views.showEmpInsure, name="showEmpInsure"),
    path('confirm', views.showConfirmInsure, name="showConfirmInsure"),
    path('selling', views.newSelling, name="newSelling"),
    path('sell', views.sellInsure, name='sellInsure'),
    path('edit/', include('insurance.edit_urls')),
    path('sellNew', views.newCusSell, name='newCusSell'),
    path('<str:id>', views.viewInsureDetail, name='viewInsureDetail'),
]