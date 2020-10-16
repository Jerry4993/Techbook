from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import UserPosts,users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','email')

class postSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPosts
        fields = ('id','author','title','desc')



class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields=('id','name','password','email')
    


        


