#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# les news qu'on trouvera sur la page d'accueil
class PostAccueil(models.Model):
    contenu = models.CharField(max_length=10000)
    auteur = models.CharField("publié par", max_length=50)
    pub_date = models.DateTimeField("publié le")
    edit_date = models.DateTimeField("modifié le")


# liste des forums, éditable que par un admin
class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    def __unicode__(self):
        return self.title


# liste des topics, un utilisateur connecté peut en rajouter un
class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
    def __unicode__(self):
        return self.title


# chaque post sur le forum
class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
    def __unicode__(self):
        return self.title
