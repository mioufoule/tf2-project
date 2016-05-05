#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    contenu = models.CharField(max_length=5000)
    auteur = modles.CharField("publié par")
    pub_date = models.CharField("publié le")
    edit_date = models.CharField("modifié le")
