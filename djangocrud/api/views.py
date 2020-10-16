from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import postSerializer,usersSerializer,UserSerializer
from .models import UserPosts,users
from rest_framework.response import Response
from .chatBotIntegration.chatbot_with_intents.Chatbot_with_intents import chat

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view, renderer_classes




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class postViewSet(viewsets.ModelViewSet):
    queryset = UserPosts.objects.all()
    serializer_class = postSerializer

    lookup_field = 'author'

    def retrieve(self,request):
        instance = self.queryset.filter(author=request.user.username)
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)

class singlePostViewSet(viewsets.ModelViewSet):
    queryset = UserPosts.objects.all()
    serializer_class = postSerializer


    def put(self,request,pk):
        instance = self.queryset.filter(id=pk).first()
        tutorial_serializer = self.serializer_class(instance, data=request.data)
        print("reached here")
        if tutorial_serializer.is_valid():
            print("reached here too")
            tutorial_serializer.save()
            return Response()
        return Response()


@api_view(('GET',))
def ChatMethod(request,querytext):
    data = chat(querytext)
    return Response(data,200)



class usersViewSet(viewsets.ModelViewSet):
    
    queryset = users.objects.all()
    serializer_class = usersSerializer



    def update(self , request , *args , **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))    
        serializer = self.serializer_class(instance, data=request.data)   
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)