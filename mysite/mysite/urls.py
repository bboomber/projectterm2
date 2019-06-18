from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from user import views as user_views
from . import views as mysite_views
from customer import views as customer_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mysite_views.showhome, name='showhome'),
    path('Q&A/', mysite_views.showQandA, name='showQandA'),
    path('contact/', mysite_views.showContact, name='showContact'),

    path('pdf/',include('insurance.pdf_urls')),

    path('employee/', include('employee_control.urls')),
    path('remind/', include('employee_control.remind_urls')),
    path('role/', include('employee_control.role_urls')),

    path('package/', include('package_control.urls')),
    path('promotion/', include('package_control.promotion_urls')),

    path('insure/', include('insurance.urls')),
    path('predict/', include('insurance.predict_urls')),
    path('report/', include('insurance.report_urls')),

    path('signup/', user_views.signup, name='signup'),
    path('profile/', include('user.profile_urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    path('customer/', include('customer.cus_urls')),
    path('car/', include('customer.car_urls')),
    
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)