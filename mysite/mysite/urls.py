from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from user import views as user_views
from . import views as mysite_views
from customer import views as customer_views

urlpatterns = [
    path('', mysite_views.showhome, name='showhome'),
    path('Q&A/', mysite_views.showQandA, name='showQandA'),

    path('employee/', include('employee_control.urls')),
    path('package/', include('package_control.urls')),
    path('promotion/', include('package_control.promotion_urls')),
    path('insure/', include('insurance.urls')),
    path('signup/', user_views.signup, name='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', include('register.urls')),

    path('customer/', include('customer.cus_urls')),
    path('car/', include('customer.car_urls')),
    
    path('admin/', admin.site.urls),
]