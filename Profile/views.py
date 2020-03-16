from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import Http404



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

import coreapi
from rest_framework.schemas import AutoSchema

from rest_framework import status
from rest_framework import generics

from Profile.models import Profile2
from Profile.models import Genero,Estado_civil,Estado,Ciudad
from Profile.models import Ocupacion

from Profile.serializer import Profile2Serializers
from Profile.serializer import GeneroSerializers,Estado_civilSerializers,OcupacionSerializers,EstadoSerializers
from Profile.serializer import CiudadSerializers



class ListAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field ('nombre'),
                coreapi.Field('apePaterno'),
                coreapi.Field('apeMaterno'),
                coreapi.Field('edad',),
                coreapi.Field('ciudad_id',),
                coreapi.Field('genero_id'),
                coreapi.Field('ocupacion_id'),
                coreapi.Field('estado_id'),
                coreapi.Field('estado_civil_id'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields  

class ProfileList2(APIView):
    permission_classes = []
    schema = ListAutoShema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile2.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = Profile2Serializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Profile2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get','put','delete'):
            extra_fields = [
                coreapi.Field('sexo'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields 

class GeneroLista(APIView):
    permission_classes = []
    schema = GeneroAutoShema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CivilAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get','put','delete'):
            extra_fields = [
                coreapi.Field('estado_civil'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields  

class EstadoCivilLista(APIView):
    permission_classes = []
    schema = CivilAutoShema()
    def get(self, request, format=None):
        print("Metodo get Estadocivil")
        queryset = Estado_civil.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = Estado_civilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Estado_civilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('ocupacion'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields 

class OcupacionLista(APIView):
    permission_classes = []
    schema = OcupacionAutoShema()
    def get(self, request, format=None):
        print("Metodo get filter ")
        queryset = Ocupacion.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get','put','delete'):
            extra_fields = [
                coreapi.Field('nombre'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields 

class EstadoLista(APIView):
    permission_classes = []
    schema = EstadoAutoShema()
    def get(self, request, format=None):
        print("Metodo get filter ")
        queryset = Estado.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CiudadAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get','put','delete'):
            extra_fields = [
                coreapi.Field('ciudad'),
                coreapi.Field('estado'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields 

class CiudadLista(APIView):
    permission_classes = []
    schema = CiudadAutoShema()
    def get(self, request, format=None):
        print("Metodo get filter ")
        queryset = Ciudad.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



