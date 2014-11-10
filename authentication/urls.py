# coding: utf-8

from django.conf.urls import patterns, url

from .views import AuthenticationView

urlpatterns = patterns('',
    url(r'^', AuthenticationView.as_view(), name='login'),
)
