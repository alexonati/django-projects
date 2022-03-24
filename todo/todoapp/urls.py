from django.contrib import admin
from django.urls import path
from .views import todoview, addtask, deletetask, edittask, edittaskview

urlpatterns = [
    path('', todoview, name='homepage'),
    path('addtask/', addtask),
    path('deletetask/<int:taskpk>/', deletetask),
    path('edittask/<int:taskpk>/', edittaskview),
    path('edittask/<int:taskpk>/update/', edittask),
]
