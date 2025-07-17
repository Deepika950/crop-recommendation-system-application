from django.urls import path
from myapp import views

urlpatterns=[
    path("",views.home,name="home"),
    path("register",views.register),
    path("login",views.login),
    path("delete",views.delete),
    path("crop2",views.crop),
    path("result",views.result),
]