from django.contrib import admin
from django.urls import include, path
from user import views as user_views

urlpatterns = [
    path('employee/', include('employee_control.urls')),
    path('signup/', user_views.signup, name='signup'),
    path('register/', include('register.urls')),
    path('admin/', admin.site.urls),
]