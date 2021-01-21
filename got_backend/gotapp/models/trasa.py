from django.db import models
from rest_framework import serializers


class Trasa(models.Model):
    nazwa = models.CharField(max_length=40)
    sumaPunkt = models.IntegerField()
    dataPocz = models.DateField()
    dataKonc = models.DateField()

    def __str__(self) -> str:
        return f'{self.id}, {self.nazwa} ({str(self.dataPocz)} ---> {str(self.dataKonc)})'


class TrasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trasa
        fields = '__all__'
