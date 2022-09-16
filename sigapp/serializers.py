from rest_framework import serializers
from .models import User_profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user_name','mobile']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = ['id','city']