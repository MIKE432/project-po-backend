from gotapp.models.region import RegionSerializer
from django.db import models
from rest_framework import serializers


class GrupaGorska(models.Model):
    kodGrupy = models.CharField(max_length=4, primary_key=True)
    nazwa = models.CharField(max_length=255)
    region = models.ForeignKey(
        'gotapp.region', on_delete=models.CASCADE)

    class Meta:
        ordering = ['kodGrupy', 'nazwa']


class GrupaGorskaSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = GrupaGorska
        fields = ['kodGrupy', 'nazwa', 'region']
