#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class PostAccueil(models.Model):
    contenu = models.CharField(max_length=10000)
    auteur = models.CharField("publié par", max_length=50)
    pub_date = models.DateTimeField("publié le")
    edit_date = models.DateTimeField("modifié le")



class Forum(models.Model):
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title


class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title


class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
