from rest_framework import serializers
from .models import Proizvod, Lokacija

class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields=('__all__')

class LokacijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokacija
        fields=('__all__')