from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('employee/', include('employee_control.urls')),
    path('register/', include('register.urls')),
    path('admin/', admin.site.urls),
]