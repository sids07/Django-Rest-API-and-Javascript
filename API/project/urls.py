from django.urls import path

from .views import register, userlogin, userlogout, CustomAuthToken
urlpatterns=[
path('signup/',register),
path('signin/',CustomAuthToken.as_view()),
path('login/',userlogin),
path('logout/',userlogout)
]