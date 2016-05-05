from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    liste_posts = Post.objects.all()
    render(request, 'siteTF2/index.html', locals())
