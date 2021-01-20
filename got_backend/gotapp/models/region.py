from django.db import models
from rest_framework import serializers


class Region(models.Model):
    region = models.CharField(max_length=255)
    class Meta:
        ordering = ['region']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'region' ]
