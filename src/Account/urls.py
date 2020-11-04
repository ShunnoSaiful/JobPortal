from django.urls import path, include
from django.contrib import admin

from .views import emp_login_page, emp_register_page

app_name = 'Account'
urlpatterns = [
    path('', emp_login_page, name='emp_login_page'),
    path('signup/', emp_register_page, name='emp_register_page'),
]
