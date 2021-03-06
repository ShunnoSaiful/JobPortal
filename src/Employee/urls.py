from django.urls import path, include
from django.contrib import admin

from .views import home, view_profile

app_name = 'Employee'
urlpatterns = [
    path('', home, name='home'),
    path('profile/<slug:slug>/', view_profile, name='view_profile'),
]
