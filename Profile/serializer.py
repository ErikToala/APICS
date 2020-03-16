from rest_framework import routers, serializers, viewsets

from Profile.models import Profile2
from Profile.models import Genero,Estado_civil,Ocupacion,Estado,Ciudad


class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')

class Estado_civilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado_civil
        fields = ('__all__')


class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')


class Profile2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Profile2
        fields = ('__all__')
