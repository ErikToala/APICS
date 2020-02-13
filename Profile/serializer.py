from rest_framework import routers, serializers, viewsets

from Profile.models import Profile2
from Profile.models import Genero,Estado_civil,Ocupacion,Estado,Ciudad


class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('sexo')

class Estado_civilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado_civil
        fields = ('estado_civil')


class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('ocupacion')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('nombre')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('ciudad','estado')


class Profile2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Profile2
        fields = ('__all__')
