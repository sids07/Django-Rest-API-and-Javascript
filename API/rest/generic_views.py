from rest_framework.generics import (CreateAPIView, 
                                    ListAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    RetrieveAPIView)
from rest_framework.filters import SearchFilter, OrderingFilter

#from django_filters.rest_framework import DjangoFilterBackend
from .serializer import InfoModelSerializer
from .models import Info

from .pagination import MyLimitOffsetPagination

class InfoModelCreateAPI(CreateAPIView):
    serializer_class = InfoModelSerializer
    '''
    As we can see default create method we came to know that to create simple get_serializer is enough 
    '''

    # we can do as above or also using default method
    #def get_serializer_class(Self):
        #we can have a look at all the factions of CreateAPIView on cdrf.co and either use default or overwrite the functions given as requirement
        #generic view means same as what we did manualy on class view but here all that are already done on helper function so no more coding is required
    #    return InfoModelSerializer

    # lets take an overwriting example (also how can we know the flow of the command)
    '''
    Here at cdrf.com we did
    1. went to post method and found it to use create method.
    2. then going to create method, and found it has several other methods and for saving perform_create was used
    3. Now, if we want to do something more than only saving serializer then we can do as below.
    '''
    def perform_create(self,serializer):
        serializer.save()
        print("Serializer Saving Done")

class InfoModelListAPI(ListAPIView):
    serializer_class = InfoModelSerializer

    pagination_class = MyLimitOffsetPagination
    '''
    Pagination is used when there is huge data and it takes lots of time to request and response.
    So, we can use pagination to limit how much data is needed and just show them.
    By default django rest framework has LimitOffsetPagination where attributes are Limit= how many to show and Offset=From where to show
    We can directly import it and use it else we can inherit this abstract class and make our own limitoffset class(which we have done creating file pagination.py.
    '''

    filter_backends= [SearchFilter, OrderingFilter]

    search_fields = ['name']
    order_fields = ['name','id']
    #filterset_fields = ['name']

    #queryset = Info.objects.all()
    
    # if static then we directly assign it as above
    # and if we need some condition checking then we use methods to define as below

    def get_queryset(self):
        return Info.objects.all() 

class InfoModelDestroyAPI(DestroyAPIView):
    queryset = Info.objects.all()
    '''
    Here from cdrf.com we can see for destroy we must need an object which is selected from self.lookup_url_kwargs or self.lookup_field
    And by default we have kwargs= 0 and fields = pk, so we must assign pk on the url to delete
    '''
class InfoModelUpdateAPI(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer

class InfoModelRetrieveAPI(RetrieveAPIView):
    serializer_class = InfoModelSerializer    