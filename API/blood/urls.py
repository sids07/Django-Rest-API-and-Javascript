from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import info_update,InfoClassBasedViews

urlpatterns=[
    path('info/',InfoClassBasedViews.as_view()),
    path('info/<int:user_id>',InfoClassBasedViews.as_view()),
    path('infoupdate/<int:pk>',info_update),
]