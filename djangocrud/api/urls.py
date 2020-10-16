from . import views
from django.contrib import admin,auth
from django.urls import path
from django.conf.urls import url,include
from djangocrud.api import views

from rest_framework import  routers      
router = routers.SimpleRouter()


router.register(r'myUser', views.usersViewSet)
router.register(r'myPosts', views.postViewSet)

urlpatterns = [
   
    path(r^'myUser', views.usersViewSet),
    path(r^'myPosts',views.postViewSet)
    
]








