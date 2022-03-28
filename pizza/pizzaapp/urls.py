from django.contrib import admin
from django.urls import path, include
from .views import authenticate_user, customerview, userloginview, signupuser, homepageview, adminloginview, adminhomepageview, authenticatedadmin, logoutadmin, addpizza, deletepizza

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('authenticatedadmin/', authenticatedadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name='homepageview'),
    path('signupuser/', signupuser),
    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/', customerview, name='customerpage'),
    path('customer/authenticate_user/', authenticate_user)
]
