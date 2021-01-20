from gotapp.models.grupa_gorska import GrupaGorskaSerializer, GrupaGorskaSerializerNested
from django.db import models
from rest_framework import serializers


class Punkt(models.Model):
    nazwa = models.CharField(max_length=255)
    wysokosc = models.FloatField()
    szerokoscGeo = models.FloatField()
    dlugoscGeo = models.FloatField()
    grupa = models.ForeignKey('gotapp.grupagorska', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazwa']


class PunktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punkt
        fields = ['id','nazwa', 'wysokosc', 'szerokoscGeo', 'dlugoscGeo', 'grupa']


class PunktSerializerNested(serializers.ModelSerializer):
    grupa = GrupaGorskaSerializerNested(read_only=True)

    class Meta:
        model = Punkt
        fields = ['id','nazwa', 'wysokosc', 'szerokoscGeo', 'dlugoscGeo', 'grupa']
