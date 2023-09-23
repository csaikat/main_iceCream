from django.contrib import admin
from django.urls import path
from module1 import views
urlpatterns = [
   
    path("",views.home,name='home'),
    path("service",views.service,name='service'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact')
]
