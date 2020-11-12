from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .serializer import AddTwoNumber, InfoSerializer
# Create your views here.

@csrf_exempt
def add_two_numbers(request):
    if request.method=="GET":
        return JsonResponse({"message":"Add two number"})

    elif request.method=="POST":
        ## post method requires csrf tokens so we import csrf_exempt to avoid error
        try:
            data = JSONParser().parse(request)
        ## JSONParser is used as we expect the input from user in json format not on form format as we were doing till now
        ## if no JSON is passed obviously JSONParser hits the error so we can write try and except command
        ## if jsonparser is not used for json data and we tried to simply do it as post form it throws 403 bad error.
        except:
            pass

        serializer = AddTwoNumber(data=data)

        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']

            result = number1 + number2
            return JsonResponse({"result":result})

        print(serializer.errors)

        return JsonResponse({"result":"Something is Wrong."},status=400)
        ## even if this is error status will still show 200 ok so we must give some error status.
        ## as we can search some https status code, we know 400 is for client error so 400 bad request may be appropriate error code for our condition.
        ## as user has given string as an input in place of integer, so send status along with JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Info
from .serializer import AddTwoNumber, InfoSerializer

## we can alway check default setting of rest_framework going to github repo of django-rest-framework
@api_view(['GET','POST'])
def add_two_numbers_rest(request):
    if request.method=="GET":
        return Response({"message":"Add two number"})
        ## since only Response is mentioned how does it know in which format does response should be made
        ## seeing default setting we may see there are listed several element for response.
        ## It performs content-negotiations, generally in which acept header client wants it search for same renderer.t
    elif request.method=="POST":
        ## post method requires csrf tokens so we import csrf_exempt to avoid error
        serializer = AddTwoNumber(data=request.data)
        #request.data vaneko similar to request.files,request.form but can only be used with rest_framework

        serializer.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']

        result = number1 + number2
        return Response({"result":result})

@api_view(['GET','POST','PUT','DELETE'])
def info_view(request,pk=None):
    if request.method=='GET':
        qs = Info.objects.all()
        #ob =Info.objects.get(id=1) Info.objects.all().first() for single object
        
        #(method 1)
        #result=[]
        #for i in qs:
            # since we are getting all instances at once i.e. iterable objects so we use loop
        #    serializer = InfoSerializer(instance=i)
        #    result.append(serializer.data)
        #    return Response(result)
        
        #(method 2)
        serializer = InfoSerializer(instance=qs,many=True)
        # simply without writing loop we can pass another arugment many=True which will tell serializer that it is iterable object so you must write loop
        # serializer converts complex query to native python and then we convert it to json file
        # since we are taking data from database and converting to json format we can directly send the instance
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = InfoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        #(method1: From views)
        #name = serializer.validated_data['name']
        #address= serializer.validated_data['address']

        #qs = Info.objects.create(
        #    name=name,
        #    address=address
        #    )
        #return Response({'msg':'ok post'}) 

        #(method2: From serializer)
        serializer.save()
        #without calling create from serializer as no instance is created it will automatically understand to go to create function 
        return Response({'msg':'ok post','result':serializer.data}) 

    elif request.method == "PUT":
        ## PUT is for full update and PATCH is for half update
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error':'Doesnot Exist'},status=404)

        #(method1: From views)
        #serializer = InfoSerializer(data=request.data)

        #serializer.is_valid(raise_exception=True)
        #name = serializer.validated_data['name']
        #address = serializer.validated_data['address']

        #obj.name = name
        #obj.address = address
        #obj.save()
        #return Response({'msg':'ok put'}) 

        #(method2:From serializer)
        serializer = InfoSerializer(data=request.data,instance=obj)
        #to hit update on serializer we must send instance attribute as well
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'ok put'}) 

    elif request.method == "DELETE":
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error':'Doesnot Exist'},status=404)

        obj.delete()
        return Response({'msg':'ok delete'}) 