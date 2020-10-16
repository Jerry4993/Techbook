from django.db import models
from datetime import datetime

  

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

class UserPosts(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=5000)
    author = models.CharField(max_length=32)

    createdOn = models.DateTimeField(blank=True)
    lastUpdatedOn = models.DateTimeField(blank=True)