from django.urls import path, include
from django.contrib import admin

from .views import job_post

app_name = 'Job'
urlpatterns = [
    path('job/', job_post, name='job_post'),
]