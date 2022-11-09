from rest_framework import serializers
from .models import UserType, User, Antrag

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        exclude = []
        

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = []


class AntragSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antrag
        exclude = []
