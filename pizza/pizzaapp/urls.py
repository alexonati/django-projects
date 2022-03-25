from django.contrib import admin
from django.urls import path, include
from .views import adminloginview, adminhomepageview, authenticatedadmin, logoutadmin

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('authenticatedadmin/', authenticatedadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
]
