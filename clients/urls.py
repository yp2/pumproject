# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from clients import views


__author__ = 'daniel'

urlpatterns = patterns(
    '',
    url(r'^$', views.ClientList.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', views.ClientDetail.as_view(), name='detail'),
    )