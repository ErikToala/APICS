from rest_framework import routers, serializers, viewsets

from Login.models import Example2

class Example2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')
