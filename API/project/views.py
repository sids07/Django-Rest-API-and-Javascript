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

from blood.models import UserInfo, Blood, Disease


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
        data=JSONParser().parse(request)
        print(data)
        serializer=Signup(data=data)
        print(data)
        if serializer.is_valid():
            name=serializer.validated_data['username']
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            confirm_password=serializer.validated_data['confirm_password']

            age = serializer.validated_data['age']

            sex = serializer.validated_data['gender']

            address = serializer.validated_data['address']
            phone = serializer.validated_data['phone']
            blood = serializer.validated_data['blood']

            disease = serializer.validated_data['disease']

            print(disease)

            print(address,phone,blood)
            pwd=set_password(password)
            cpwd=set_password(confirm_password)

            print(pwd)
            print(data)

            user=User.objects.create(username=name,email=email,password=pwd)

            b_group = Blood.objects.get_or_create(group=blood)
            print(user)
            userinfo = UserInfo.objects.create(user=user,blood=b_group[0],name=name,age=age,gender=sex,blood_group=blood,phone=phone,address=address)
            for d in disease:
                print(d)
                disease_obj = Disease.objects.get_or_create(dis_name=d)
                userinfo.disease.add(disease_obj[0])

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