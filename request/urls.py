# coding: utf-8

from django.conf.urls import patterns, url
from .views import RequestCreateView, RequestListView

urlpatterns = patterns('',
	url(r'register/$', RequestCreateView.as_view(), name='register',),
    url(r'list/$', RequestListView.as_view(), name='list',),
	url(r'list/(?P<status>\w+)/$', RequestListView.as_view(), name='list.by.status',),
)