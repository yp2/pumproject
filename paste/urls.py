# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
    url('^paste/$', views.PasteList.as_view(), name='list'),
    url('^paste/(?P<id>\d+)$', views.PasteDetail.as_view(), name='detail'),
    url('^paste/author/(?P<author>.*)$', views.PasteList.as_view(), name='author_paste')
    )
