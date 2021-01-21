from gotapp.models.punkt import PunktSerializerNested
from django.db import models
from rest_framework import serializers


class Odcinek(models.Model):
    nazwa = models.CharField(max_length=255)
    przewyzszenie = models.FloatField()
    dlugosc = models.FloatField()
    czyAktywny = models.BooleanField()
    dataPonOtw = models.DateField(blank=True, null=True)
    punktacja = models.IntegerField(blank=True, null=True)
    rokAkt = models.DateField(blank=True, null=True)
    discriminator = models.CharField(max_length=10)
    poczatek = models.ForeignKey(
        'gotapp.Punkt', related_name='zaczynane', on_delete=models.CASCADE)
    koniec = models.ForeignKey(
        'gotapp.Punkt', related_name='konczone', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazwa', 'dlugosc', 'czyAktywny']

    def __str__(self) -> str:
        return f'{self.nazwa} ({str(self.poczatek)}  ---> {str(self.koniec)})'


class OdcinekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odcinek
        fields = '__all__'


class OdcinekSerializerNested(OdcinekSerializer):
    poczatek = PunktSerializerNested(read_only=True)
    koniec = PunktSerializerNested(read_only=True)