from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/',login_view, name='login'),
    path('menu/',menu, name='menu'),
]
