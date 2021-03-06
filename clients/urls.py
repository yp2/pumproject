# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from clients import views


__author__ = 'daniel'

urlpatterns = patterns(
    '',
    url(r'^$', views.ClientList.as_view(), name='list'),
    url(r'^(?P<username>\w+)/$', views.ClientList.as_view(), name='list-client-user'),
    url(r'^(?P<username>\w+)/(?P<remote_id>\d+)/$', views.ClientDetail.as_view(), name='detail'),
    )