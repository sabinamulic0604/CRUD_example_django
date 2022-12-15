from rest_framework import serializers
from .models import Proizvod, Lokacija

class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields=('__all__')
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class LokacijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokacija
        fields=('__all__')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


