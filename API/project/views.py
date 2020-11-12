from django.shortcuts import render

from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .models import User, set_password
from .serializer import Signup, UserLoginSerializer

from django.contrib.auth import login, logout
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from blood.models import UserInfo


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@csrf_exempt
def register(request):
    if request.method=='GET':
        qs=User.objects.all()
        serializer = Signup(instance=qs,many=True)
        return JsonResponse({'message':'Hello','result':serializer.data})
    
    else:
        #data=JSONParser().parse(request)
        print(request.POST)
        serializer=Signup(data=request.POST)
        print(request.POST['age'])
        if serializer.is_valid():
            name=serializer.validated_data['username']
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            confirm_password=serializer.validated_data['confirm_password']
            
            pwd=set_password(password)
            cpwd=set_password(confirm_password)

            print(pwd)
            print(data)

            user=User.objects.create(username=name,email=email,password=pwd,confirm_password=cpwd)
            print(data)
            userinfo = UserInfo.objects.create(user=user,name=name,image=data['myimg'].files[0],blood_group=data['inputBlood'].value, phone=data['inputNumber'].value, age=data['inputAge4'].value,  gender=data['inputSex'].value, address=data['inputAddress'].value)
            print(serializer.data)
            return JsonResponse({'msg':'ok post','result':serializer.data},status=status.HTTP_201_CREATED)
            #return JsonResponse(serializer.data)

        print(serializer.errors)

        return JsonResponse({"result":serializer.errors},status=400)

@csrf_exempt
def userlogin(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return JsonResponse({ 'success': 'You are logged in successfully'},status=200)
        print(serializer.errors)

        return JsonResponse({"result":serializer.errors},status=400)

@csrf_exempt
def userlogout(request):
    if request.method=='POST':
        logout(request)
        return JsonResponse({'success':'You are logged out successfully'})