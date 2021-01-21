from gotapp.models.ksiazeczka import KsiazeczkaSerializer, KsiazeczkaSerializerNested
from gotapp.models.legitymacja import LegitymacjaSerializer
from django.db import models
from rest_framework import serializers


def plecValidator(value: str):
    if not value in ('K', 'M'):
        raise serializers.ValidationError(
            'plec field must be either "K" for female or "M" for male')


class Osoba(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    plec = models.CharField(max_length=1, blank=True,
                            null=True, validators=[plecValidator])
    dataUr = models.DateField()
    email = models.EmailField(unique=True)
    haslo = models.CharField(max_length=64)
    czyAkt = models.BooleanField()
    czyNiepeln = models.BooleanField()
    miasto = models.CharField(max_length=100, blank=True, null=True)
    ulica = models.CharField(max_length=100, blank=True, null=True)
    nrDomu = models.IntegerField(blank=True, null=True)
    nrMieszk = models.IntegerField(blank=True, null=True)
    kodPoczt = models.CharField(max_length=64, blank=True, null=True)
    nrTel = models.CharField(max_length=12, blank=True, null=True)
    discriminator = models.CharField(max_length=15)
    wycieczki = models.ManyToManyField(
        'gotapp.Wycieczka', through='gotapp.Uczestnictwo')

    def __str__(self) -> str:
        return f'{self.id}, {self.imie} {self.nazwisko} - {self.discriminator}'

    class Meta:
        ordering = ['discriminator', 'nazwisko', 'imie']


class OsobaSerializer(serializers.ModelSerializer):
    legitymacja = serializers.PrimaryKeyRelatedField(
        read_only=True, allow_null=True)
    ksiazeczka = serializers.PrimaryKeyRelatedField(
        read_only=True, allow_null=True)

    class Meta:
        model = Osoba
        fields = '__all__'


class OsobaSerializerNested(OsobaSerializer):
    legitymacja = LegitymacjaSerializer(read_only=True)
    ksiazeczka = KsiazeczkaSerializerNested(read_only=True)
