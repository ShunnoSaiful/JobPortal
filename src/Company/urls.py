from django.urls import path, include
from django.contrib import admin

from .views import view_profile

app_name = 'Company'
urlpatterns = [
    path('profile/<slug:slug>/', view_profile, name='view_profile'),
]
