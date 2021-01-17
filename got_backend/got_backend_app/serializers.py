import re
from typing import Dict
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from got_backend_app.models import GrupaGorska, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['idreg', 'region']

    def create(self, validated_data: Dict) -> Region:
        """
        Create and return a new `Region` instance, given the validated data.
        """
        return Region.objects.create(**validated_data)

    def update(self, instance: Region, validated_data: Dict) -> Region:
        """
        Update and return an existing `Region` instance, given the validated data.
        """
        instance.region = validated_data.get('region', instance.region)
        instance.save()
        return instance


class GrupaGorskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupaGorska
        fields = ['kodgrupy', 'nazwa', 'idreg']


    def create(self, validated_data: Dict) -> GrupaGorska:
        """
        Create and return a new `GrupaGorska` instance, given the validated data.
        """
        return GrupaGorska.objects.create(**validated_data)

    def update(self, instance: GrupaGorska, validated_data: Dict) -> GrupaGorska:
        """
        Update and return an existing `GrupaGorska` instance, given the validated data.
        """
        instance.nazwa=validated_data.get('nazwa', instance.nazwa)
        instance.idreg=validated_data.get('idreg', instance.idreg)
        instance.save()
        return instance
