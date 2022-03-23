from django.contrib import admin
from django.urls import path

from .views import helloworld, hellostudent

urlpatterns = [
    path('helloworld/', helloworld),
    path('hellostudent/', hellostudent)
]
