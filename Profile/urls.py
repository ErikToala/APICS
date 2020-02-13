from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets

from Profile import views

urlpatterns = [
    #re_path(r'Profile/$', CustonAuthToken.as_view()),
    re_path(r'ejercicio_profile/$',views.ProfileList2.as_view()),
    re_path(r'ejercicio_profile/genero/$', views.GeneroLista.as_view()),
    re_path(r'ejercicio_profile/estado_civil/$', views.EstadoCivilLista.as_view()),
    re_path(r'ejercicio_profile/ocupacion/$', views.OcupacionLista.as_view()),
    re_path(r'ejercicio_profile/estado/$', views.EstadoLista.as_view()),
    re_path(r'ejercicio_profile/ciudad/$', views.CiudadLista.as_view()),
    

    #Hola soy Erik
]