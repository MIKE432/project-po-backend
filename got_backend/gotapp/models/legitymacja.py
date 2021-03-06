from gotapp.models.uprawnienie import UprawnienieSerializer
from django.db import models
from rest_framework import serializers


class Legitymacja(models.Model):
    terminWaz = models.DateField()
    dataPrzyznania = models.DateField()
    przod = models.OneToOneField('gotapp.Osoba', on_delete=models.CASCADE,
                                 related_name='legitymacja')
    uprawnienia = models.ManyToManyField(
        'gotapp.GrupaGorska', through='gotapp.Uprawnienie')

    def __str__(self) -> str:
        return f'legitymacja: {str(self.przod)}'


class LegitymacjaSerializer(serializers.ModelSerializer):
    uprawnienia_set = UprawnienieSerializer(many=True, read_only=True)

    class Meta:
        model = Legitymacja
        fields = '__all__'
