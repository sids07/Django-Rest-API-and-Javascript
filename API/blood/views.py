import os

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import UserInfo
from .serializer import UserInfoSerializer

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class InfoClassBasedViews(APIView):
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]

    def get(self,request,user_id=None):
        if user_id:
            try:
                obj = UserInfo.objects.get(user_id=user_id)
            except UserInfo.DoesNotExist:
                return Response({'error':'Doesnot Exist'},status=404)
            serializer = UserInfoSerializer(instance=obj)
            return Response(serializer.data)
                    
        a=UserInfo.objects.all()
        serializer = UserInfoSerializer(instance=a, many=True)
        return Response(serializer.data)
        #same code as function view

    def post(self,request,*args,**kwargs):

        serializer= UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response({'msg':'ok post','result':serializer.data},status=201)
        return Response({'msg':'ok post','result':serializer.data},status=status.HTTP_201_CREATED) 

        #directly status= 201 seems to be confusing and not so standard so rest_framework giving status model which have list of status code in more readable format
    
    def put(self,request,user_id):
        try:
            obj = UserInfo.objects.get(user_id=user_id)
        except UserInfo.DoesNotExist:
            return Response({'error':'Doesnot Exist'},status=404)

        os.remove(obj.image.path)
        serializer = UserInfoSerializer(data=request.data,instance=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'ok put'}) 
    
    def patch(self,request,user_id):
        try:
            obj = UserInfo.objects.get(user_id=user_id)
        except UserInfo.DoesNotExist:
            return Response({'error':'Doesnot Exist'},status=404)

        #os.remove(info.image.path)
        serializer = UserInfoSerializer(data=request.data,instance=obj,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'ok patch'})

    def delete(self,request,user_id):
        try:
            obj = UserInfo.objects.get(user_id)
        except UserInfo.DoesNotExist:
            return Response({'error':'Doesnot Exist'},status=404)

        obj.delete()
        return Response({'msg':'ok delete'}) 

class InfoCreateAPIView(CreateAPIView):
    serializer_class=UserInfoSerializer
    authentication_classes=[SessionAuthentication,]

@api_view(['PUT', 'PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
def info_update(request, pk):
    try:
        info = UserInfo.objects.get(pk=pk)

    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        os.remove(info.image.path)
        serializer=UserInfoSerializer(info,data=request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':

        serializer=UserInfoSerializer(info,data=request.data,partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = info.delete()
        data = {}
        if operation:
            data['success'] = 'Deleted successfully'
        else:
            data['error'] = 'Delete failed'
        return Response(data=data)



