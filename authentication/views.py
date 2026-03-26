from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import *

class UserView(APIView):
    def post(self,request):
        new_user=User(username=request.data['username'],is_superuser=request.data['is_superuser'],ph_no=request.data['ph_no'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response("new user Created")

class UserLoginView(APIView):
    def post(self,request):
        user_verify=authenticate(username=request.data['username'],password=request.data['password'])
        if user_verify==None:
            return Response("name or password is invalid")
        return Response("Login")


