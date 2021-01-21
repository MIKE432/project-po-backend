from gotapp.models.grupa_gorska import GrupaGorska
from django.db import models
from rest_framework import serializers


class Uprawnienie(models.Model):
    dataWaznosci = models.DateField()
    dataPrzyznania = models.DateField()
    legitymacja = models.ForeignKey(
        'gotapp.Legitymacja', on_delete=models.CASCADE, related_name='uprawnienia_set')
    grupaGorska = models.ForeignKey(
        'gotapp.GrupaGorska', on_delete=models.CASCADE)


class UprawnienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uprawnienie
        fields = '__all__'
