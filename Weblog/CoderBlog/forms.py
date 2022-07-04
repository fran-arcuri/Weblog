from turtle import title
from django import forms
from django.db import models
from .models import *

class CreatePost(forms.ModelForm):

   class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'author', 'creation_date')