from django.urls import path

from .views import add_two_numbers, add_two_numbers_rest,info_view
from .class_view import InfoClassBasedViews
from .generic_views import InfoModelCreateAPI,InfoModelListAPI, InfoModelDestroyAPI, InfoModelUpdateAPI, InfoModelRetrieveAPI

from .viewset_views import InfoModelViewSet

from rest_framework.routers import DefaultRouter
from django.conf.urls import include

r = DefaultRouter()
'''
Usually for viewset we mention path as below:
path('info/view-set/',InfoModelViewSet(actions=['get':'list','post':'create']))

As viewset is used to do CRUD operation all along so we must give action parameters.
But giving action parameter and assigning dictionary seems little time consuming so rest_framework has given DefaultRouter() which can be used to assign path.
Now we can used .register method to assign path.
And finally add urls of object to urlpatterns.
'''
r.register('info/view-set',InfoModelViewSet)

urlpatterns=[
    path('project/',include('project.urls')),
    path('blood/',include('blood.urls')),
    path('add/',add_two_numbers),
    path('v2/add/',add_two_numbers_rest),

    path('info',info_view),
    path('info/<int:pk>',info_view),

    path('info/class-based/',InfoClassBasedViews.as_view()),

    path('info/generic/create',InfoModelCreateAPI.as_view()),
    path('info/generic/list',InfoModelListAPI.as_view()),
    path('info/generic/destroy/<int:pk>',InfoModelDestroyAPI.as_view()),
    path('info/generic/update/<int:pk>',InfoModelUpdateAPI.as_view()),
    path('info/generic/retrieve/<int:pk>',InfoModelRetrieveAPI.as_view())
]+ r.urls