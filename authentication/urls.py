# coding: utf-8

from django.conf.urls import patterns, url

from .views import AuthenticationLoginView, AuthenticationLogoutView

urlpatterns = patterns('',
    url(r'^$', AuthenticationLoginView.as_view(), name='login'),
    url(r'^logout$', AuthenticationLogoutView.as_view(), name='logout'),
)
