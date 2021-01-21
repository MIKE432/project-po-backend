from django.db import models
from rest_framework import serializers


class Wycieczka(models.Model):
    nazwa = models.CharField(max_length=40)
    dataPocz = models.DateField()
    dataKonc = models.DateField()
    uczestnicy = models.ManyToManyField(
        'gotapp.Osoba', through='gotapp.Uczestnictwo')

    class Meta:
        ordering = ['nazwa', 'dataPocz', 'dataKonc']

    def __str__(self) -> str:
        return f'{self.nazwa} ({str(self.dataPocz)} - {str(self.dataKonc)})'


class WycieczkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wycieczka
        fields = '__all__'
