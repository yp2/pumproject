# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
    url('^$', views.PasteList.as_view(), name='list'),
    url('^(?P<id>\d+)/$', views.PasteDetail.as_view(), name='detail'),
    url('^author/(?P<author>.*)$', views.PasteList.as_view(), name='author_paste')
    )
