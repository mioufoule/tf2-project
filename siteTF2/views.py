  #!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

import datetime

# renvoie la liste des news de l'accueil au template index.html
def index(request):
    PostAccueil_list = PostAccueil.objects.all()
    return render(request, 'siteTF2/index.html', locals())


def forum(request):
    forum_list = Forum.objects.all()
    return render(request, 'siteTF2/forum.html', locals())


def thread(request, forum_id):

    forum = Forum.objects.get(id = forum_id)
    thread_list = Thread.objects.filter(forum=forum).values()
    forum_title = forum.title
    return render_to_response("siteTF2/thread.html", locals())
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            thread = Post( thread = thread_info )
            form = PostForm(request.POST, instance = thread )
            form.save()
            return HttpResponseRedirect(reverse('forum.views.post_dir',
                                                args=(thread_id,)))
    else:
        form = PostForm()
    return render_to_response("forum/post.html",
                              {'post_list' : post_list,
                               'thread_info' : thread_info,
                               'form': form,},
                              context_instance=RequestContext(request) )


def post(request, forum_id, thread_id):
    thread_info = Thread.objects.get(pk=thread_id)
    post_list = Post.objects.filter( thread = thread_id )
    return render_to_response("siteTF2/post.html",
                              {'post_list' : post_list, 'thread_info' : thread_info,},
                              context_instance=RequestContext(request) )



def ajouterForum(request):
    titrePage = 'ajouter un forum'
    submit = 'ajouter le forum'
    if request.method == 'POST': #  If the form has been submitted...
        form = ForumForm(request.POST) #  A form bound to the POST data
        if form.is_valid(): #  All validation rules pass
            forum = Forum()
            forum.title = form.cleaned_data['title']
            forum.description = form.cleaned_data['description']
            form.save()
            return HttpResponseRedirect(reverse('siteTF2:forum'))
    else:
        form = ForumForm() # An unbound form
        return render(request, 'siteTF2/ajouter.html', locals())


def ajouterThread(request, forum_id):
    titrePage = 'ajouter un sujet'
    submit = 'ajouter le sujet'
    if request.method == 'POST': #  If the form has been submitted...
        form = ThreadForm(request.POST) #  A form bound to the POST data
        if form.is_valid(): #  All validation rules pass
            thread = Thread()
            thread.forum = Forum.objects.get(id=forum_id)
            thread.title = form.cleaned_data['title']
            thread.content = form.cleaned_data['content']
            thread.pub_date = datetime.datetime.now()
            thread.save()
            return HttpResponseRedirect(reverse('siteTF2:thread',
                                                args=(forum_id,)))
    else:
        form = ThreadForm() # An unbound form
        return render(request, 'siteTF2/ajouter.html', locals())
