from django.conf import settings
from django.conf.urls.static import static

from .views import home,signup,login
from django.urls import path
from .views import home,signup,login,donate,profile, donation_form, donation,form, search

urlpatterns = [
    path('',home),
    path('doner/',donate),
    path('signup/',signup),
    path('login/',login),
    path('profile',profile),
    path('create_form',donation_form),
    path('donation_form',donation),
    path('update',form),
    path('search',search)
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)