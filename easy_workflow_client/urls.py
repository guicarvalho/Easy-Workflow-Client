from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('dashboard.urls', namespace='dashboard'),),
    url(r'^login/', include('authentication.urls', namespace='authentication'),),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard'),),
    url(r'^profile_user/', include('profile_user.urls', namespace='profile_user'),),
    url(r'^request/', include('request.urls', namespace='request'),),
)
