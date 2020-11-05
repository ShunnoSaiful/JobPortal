from django.urls import path, include
from django.contrib import admin

from .views import job_post, job_list, job_details

app_name = 'Job'
urlpatterns = [
    path('job/', job_post, name='job_post'),
    path('job/list/', job_list, name='job_list'),
    path('job/<slug:slug>/', job_details, name='job_details'),
]