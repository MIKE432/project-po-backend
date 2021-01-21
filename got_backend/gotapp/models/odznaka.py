from gotapp.models.rodzaj_odznaki import RodzajOdznakiSerializer
from gotapp.models.stopien_odznaki import StopienOdznakiSerializer
from django.db import models
from rest_framework import serializers


class Odznaka(models.Model):
    dataPrzyznania = models.DateField(blank=True, null=True)
    wyPkt = models.IntegerField()
    czyRozp = models.BooleanField(blank=True, null=True)
    stopien = models.ForeignKey(
        'gotapp.StopienOdznaki', on_delete=models.CASCADE)
    rodzaj = models.ForeignKey(
        'gotapp.RodzajOdznaki', on_delete=models.CASCADE)
    ksiazeczka = models.ForeignKey(
        'gotapp.Ksiazeczka', on_delete=models.CASCADE, related_name='odznaki')

    class Meta:
        ordering = ['dataPrzyznania']

    def __str__(self):
        return f'{self.rodzaj} {self.stopien} - {self.ksiazeczka}'


class OdznakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odznaka
        fields = '__all__'


class OdznakaSerializerNested(OdznakaSerializer):
    stopien = StopienOdznakiSerializer(read_only=True)
    rodzaj = RodzajOdznakiSerializer(read_only=True)
