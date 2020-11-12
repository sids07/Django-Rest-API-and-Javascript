from rest_framework.viewsets import ModelViewSet
from .serializer import InfoModelSerializer
from .models import Info

class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()

    http_method_names = ['get', 'post', 'patch', 'head', 'delete','put']

    #above 2 variable are basic variables for viewsets
    #for listing and retrieving objects will be retrived as queryset and for others queryset is not of much need
