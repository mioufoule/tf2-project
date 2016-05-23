from django.forms import ModelForm
from .models import *


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['forum', 'pub_date']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['thread']
