from gotapp.models.osoba import OsobaSerializer
from django.db import models
from rest_framework import serializers
from gotapp.models.trasa import TrasaSerializer, TrasaSerializerNested


class Wycieczka(models.Model):
    nazwa = models.CharField(max_length=40)
    dataPocz = models.DateField()
    dataKonc = models.DateField()
    uczestnicy = models.ManyToManyField(
        'gotapp.Osoba', through='gotapp.Uczestnictwo')
    trasa = models.OneToOneField('gotapp.Trasa', on_delete=models.CASCADE,
                                 related_name='wycieczka', null=True, blank=True)

    class Meta:
        ordering = ['nazwa', 'dataPocz', 'dataKonc']

    def __str__(self) -> str:
        return f'{self.nazwa} ({str(self.dataPocz)} - {str(self.dataKonc)})'


class WycieczkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wycieczka
        fields = '__all__'


class WycieczkaSerializerNested(serializers.ModelSerializer):
    trasa = TrasaSerializerNested(read_only=True)
    uczestnicy = OsobaSerializer(read_only=True, many=True)

    class Meta:
        model = Wycieczka
        fields = '__all__'
