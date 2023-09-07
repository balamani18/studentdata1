from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',loadpage),
    path('s/',start),
    path('u/',upd),
    path('d/',delt),
    path('sd/',std),
    path('sdu/',upmark),
    path('dm/',delmark),
    path('st/',stuinfo),
    path('up/',updateinfo),
    path('dl/',deleteinfo),
    path('stdm/',stdmarks),
    path('stdupm/',updtmark),
    path('dltm/',deletemark)
]