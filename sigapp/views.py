from django.shortcuts import render
from .models import User_profile,User

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sigapp.serializers import UserProfileSerializer, UserSerializer

@api_view(['GET', 'POST'])
def Student_profile(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = User_profile.objects.all()
        serializer = UserProfileSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)