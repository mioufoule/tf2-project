#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    contenu = models.CharField(max_length=5000)
    auteur = models.CharField("publié par", max_length=50)
    pub_date = models.DateTimeField("publié le")
    edit_date = models.DateTimeField("modifié le")
