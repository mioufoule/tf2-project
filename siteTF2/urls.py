#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forum/$', views.forum, name="forum"),
    url(r'^forum/(?P<forum_id>\d+)/$', views.thread, name="thread"),
    url(r'^forum/(?P<forum_id>\d+)/thread/(?P<thread_id>\d+)/$', views.post, name="post"),
]
