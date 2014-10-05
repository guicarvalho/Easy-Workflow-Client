# coding: utf-8

from django.conf.urls import patterns, url
from .views import UserProfileCreateView

urlpatterns = patterns('',
	url(r'^register/$', UserProfileCreateView.as_view(), name='register',),
)