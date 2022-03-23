from django.contrib import admin
from django.urls import path

from .views import counter, decrement, reset, increment

urlpatterns = [
    path('counter/', counter),
    path('increment/', increment),
    path('decrement/', decrement),
    path('reset/', reset)

]
