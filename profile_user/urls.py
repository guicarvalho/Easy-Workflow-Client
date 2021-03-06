# coding: utf-8

from django.conf.urls import patterns, url
from .views import UserProfileView, UserProfileListView

urlpatterns = patterns('',
	url(r'register/$', UserProfileView.as_view(), name='register',),
	url(r'list/$', UserProfileListView.as_view(), name='list',),
)