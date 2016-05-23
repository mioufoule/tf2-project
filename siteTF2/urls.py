#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # afficher les entrées
    url(r'^$', views.index, name='index'),
    url(r'^forum/$', views.forum, name="forum"),
    url(r'^forum/(?P<forum_id>\d+)/$', views.thread, name="thread"),
    url(r'^forum/(?P<forum_id>\d+)/thread/(?P<thread_id>\d+)/post/$',
        views.post, name="post"),
    # ajout d'entrées
    url(r'^forum/add/$', views.ajouterForum, name="ajouterForum"),
    url(r'^forum/(?P<forum_id>\d+)/add/$', views.ajouterThread,
        name="ajouterThread"),
]
