from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    creation_date = models.DateTimeField(default=timezone.now)
    #creation_date = models.DateTimeField(auto_now_add=True)
    #creation_date = models.DateField(default=datetime.now)

    #author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    author = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='pictures', blank=True, default=None, null=False)

    def __str__(self):
        return self.title+", Categoria:"+str(self.category)