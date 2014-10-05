# coding: utf-8

from django.conf.urls import patterns, url
from .views import RequestCreateView

urlpatterns = patterns('',
	url(r'^register/$', RequestCreateView.as_view(), name='register',),
)