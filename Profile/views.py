from django.shortcuts import render
from rest_framework_swagger.views import get_swagger_view

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from Profile.models import Profile2
from Profile.models import Genero,Estado_civil,Estado,Ciudad
from Profile.models import Ocupacion


from Profile.serializer import Profile2Serializers
from Profile.serializer import GeneroSerializers,Estado_civilSerializers,OcupacionSerializers,EstadoSerializers
from Profile.serializer import CiudadSerializers


schema_view = get_swagger_view(title='Pastebin API')

class GeneroLista(APIView):
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


class EstadoCivilLista(APIView):
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


class OcupacionLista(APIView):
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



class EstadoLista(APIView):
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


class CiudadLista(APIView):
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
    

class ProfileList2(APIView):
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



