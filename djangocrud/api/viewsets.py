from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import postSerializer,usersSerializer,UserSerializer
from .models import post,users
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer


class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = usersSerializer



    def update(self , request , *args , **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))    
        serializer = self.serializer_class(instance, data=request.data)   
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]