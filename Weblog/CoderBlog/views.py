from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render_to_response
from .models import *
from .forms import *

# Create your views here.
def home(request):
    posts = Post.objects.order_by("-creation_date")
    return render_to_response("home.html", {"posts":posts})

def about(request):
    return render(request, 'about.html')

def pages(request):
    return render(request, 'pages.html')

def post(request, idpost):
    post = Post.objects.get(id=idpost)
    return render_to_response("post.html", {"post":post})

def search_by_category(request, idcategoria):
    category = Categoria.objects.get(id=idcategoria)
    posts = category.post_set.order_by("-creation_date")
    return render_to_response( "home.html", {"posts":posts})


def createPost(request):
    form = CreatePost(request.POST)
    if form.is_valid():
        new_post = Post(title=form['title'], content=form['content'], category=form['category'],
        creation_date=form['creation_date'], author=form['author'])
        new_post.save()
        return render(request, 'home.html')
    return render(request, 'createPost.html', {'form':form})
    


#def createPost(request):
#    form = CreatePost(request.POST)
#    if request.method == 'POST':
#        if form.is_valid():
#            information = request.cleaned_data
#        title=information['title']
#        content=information['content']
#        category=information['category']
#        creation_date=information['creation_date']
#        author=information['author']
#        post = Post(title=title, content=content, category=category, creation_date=creation_date, author=author)
#        post.save()
#        return render(request, 'home.html')
#    else:
#        request = CreatePost()
#    return render(request, "createPost.html", {'form':form})