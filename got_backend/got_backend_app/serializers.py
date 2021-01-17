from typing import Dict
from django.db import models
from rest_framework import serializers
from got_backend_app.models import GrupaGorska, Legitymacja, Odcinek, Region, Ksiazeczka


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
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.idreg = validated_data.get('idreg', instance.idreg)
        instance.save()
        return instance


class KsiazeczkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazeczka
        fields = ['idksiazki', 'idturysty', 'punktacja']

    def create(self, validated_data: Dict) -> Ksiazeczka:
        """
        Create and return a new `Ksiazeczka` instance, given the validated data.
        """
        return Ksiazeczka.objects.create(**validated_data)

    def update(self, instance: Ksiazeczka, validated_data: Dict) -> Ksiazeczka:
        """
        Update and return an existing `Ksiazeczka` instance, given the validated data.
        """
        instance.punktacja = validated_data.get(
            'punktacja', instance.punktacja)
        instance.save()
        return instance


class LegitymacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legitymacja
        fields = ['nrlegi', 'idprzod', 'terminwazn', 'dataprzyznania']

    def create(self, validated_data: Dict) -> Legitymacja:
        """
        Create and return a new `Legitymacja` instance, given the validated data.
        """
        return Legitymacja.objects.create(**validated_data)

    def update(self, instance: Legitymacja, validated_data: Dict) -> Legitymacja:
        """
        Update and return an existing `Legitymacja` instance, given the validated data.
        """
        instance.terminwazn = validated_data.get(
            'terminwazn', instance.terminwazn)
        instance.dataprzyznania = validated_data.get(
            'dataprzyznania', instance.terminwazn)
        instance.save()
        return instance


class OdcinekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legitymacja
        fields = ['idodc', 'idpoczatek', 'idkoniec', 'nazwa', 'przewyzszenie',
                  'dlugosc', 'czyaktywny', 'dataponotw', 'punktacja', 'rokakt', 'discriminator']

    def create(self, validated_data: Dict) -> Odcinek:
        """
        Create and return a new `Odcinek` instance, given the validated data.
        """
        return Odcinek.objects.create(**validated_data)

    def update(self, instance: Odcinek, validated_data: Dict) -> Odcinek:
        """
        Update and return an existing `Odcinek` instance, given the validated data.
        """
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.przewyzszenie = validated_data.get(
            'przewyzszenie', instance.przewyzszenie)
        instance.dlugosc = validated_data.get('dlugosc', instance.dlugosc)
        instance.czyaktywny = validated_data.get(
            'czyaktywny', instance.czyaktywny)
        instance.dataponotw = validated_data.get(
            'dataponotw', instance.dataponotw)
        instance.punktacja = validated_data.get(
            'punktacja', instance.punktacja)
        instance.discriminator = validated_data.get(
            'discriminator', instance.discriminator)
        instance.rokakt = validated_data.get('rokakt', instance.rokakt)
        instance.save()
        return instance
        