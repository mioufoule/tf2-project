#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^siteTF2/', include('siteTF2.urls')),
    url(r'^admin/', admin.site.urls),
]
