from django.forms import ModelForm
from .models import *

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ('forum')

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('thread')
