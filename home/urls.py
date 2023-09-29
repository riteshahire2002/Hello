from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("standard",views.standard,name='standard'),
    path("generic",views.generic,name='generic'),
    path("ayurvedic",views.ayurvedic,name='ayurvedic')
]
