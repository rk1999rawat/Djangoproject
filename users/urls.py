from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),#""-->localhost/users/
    path("home/",views.home),#localhost/users/home
    path("singin/",views.login),#localhost/users/signin
    path("singup/",views.singup),#localhost/users/
    path("aftersignup/",views.aftersignup),#localhost/users/

] 