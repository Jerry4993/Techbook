"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin,auth
from django.urls import path
from django.conf.urls import url,include
from djangocrud.api import views


from rest_framework import  routers      

from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
 

router = routers.DefaultRouter()
router.register(r'users/', views.UserViewSet)
router.register(r'api/myUser', views.usersViewSet)


router.register(r'api/myPosts/', views.postViewSet ,basename='UserPost')




urlpatterns = [
   
    path('', include(router.urls)),
    path('users/', views.UserViewSet),
    path('api/myUser', views.usersViewSet),
    # path('api/myPosts',views.postViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/myPosts/', views.postViewSet.as_view({'get': 'retrieve'})),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('api/chat/<str:querytext>',views.ChatMethod),
    path('api/myPosts/<int:id>',views.singlePostViewSet)
]
