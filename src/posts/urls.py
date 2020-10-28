from django.conf.urls import url
from django.urls import path, include

from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	PostDetailView,
	company,
	companyprofile,
	forumpostview,
	jobs,
	profilesetting,
	profile,
	signin,
	userprofile,
	forum
	)
app_name = 'posts'
urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'), #Django Code Review #3 on joincfe.com/youtube/
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),




    url(r'^companyprofile/$', companyprofile),
    url(r'^forumpostview/$', forumpostview),
    url(r'^forum/$', forum),
    url(r'^jobs/$', jobs),
    url(r'^profilesetting/$', profilesetting),
    url(r'^profile/$', profile),
    url(r'^signin/$', signin),
    url(r'^userprofile/$', userprofile),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    path('company/', company, name='company'),
    
]