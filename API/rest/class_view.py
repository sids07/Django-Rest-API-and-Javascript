from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Info
from .serializer import InfoSerializer, InfoModelSerializer


class InfoClassBasedViews(APIView):

    def get(self,request,*args,**kwargs):
        qs = Info.objects.all()
        serializer = InfoSerializer(instance=qs,many=True)
        return Response(serializer.data)
        #same code as function view

    def post(self,request,*args,**kwargs):
        current_time = timezone.now()
        print("current_time",current_time)

        context= {
            'current_time':current_time
        }
        # if we want to send data to serializer from here we can make context as above and send it to serializer with argument context and use it on serializer as self.context
        #serializer = InfoSerializer(data=request.data,context=context)
        serializer= InfoModelSerializer(data=request.data,context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response({'msg':'ok post','result':serializer.data},status=201)
        return Response({'msg':'ok post','result':serializer.data},status=status.HTTP_201_CREATED) 

        #directly status= 201 seems to be confusing and not so standard so rest_framework giving status model which have list of status code in more readable format