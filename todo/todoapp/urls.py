from django.contrib import admin
from django.urls import path
from .views import todoview

urlpatterns = [
    path('', todoview)
]
