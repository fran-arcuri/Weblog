from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/<idpost>', post, name='post'),
    path('category/<idcategoria>', search_by_category, name='search_by_category'),
    path('about/', about, name='about'),
    path('pages/', pages, name='pages'),

    path('createPost/', createPost, name='createPost'),
]