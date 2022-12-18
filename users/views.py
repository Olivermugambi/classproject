from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User_Serializer,Register_User_Serializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details 
# using Token Authentication
class UserDetailAPIView(APIView):
  authentication_classes = (TokenAuthentication,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = User_Serializer(user)
    return Response(serializer.data)

# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = Register_User_Serializer
