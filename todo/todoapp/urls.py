from django.contrib import admin
from django.urls import path
from .views import todoview, addtask

urlpatterns = [
    path('', todoview),
    path('addtask/', addtask)
]
