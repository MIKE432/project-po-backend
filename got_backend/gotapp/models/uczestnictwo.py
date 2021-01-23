from django.db import models
from rest_framework import serializers


class Uczestnictwo(models.Model):
    turysta = models.ForeignKey('gotapp.Osoba', on_delete=models.CASCADE)
    wycieczka = models.ForeignKey('gotapp.Wycieczka', on_delete=models.CASCADE)
    opis = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        unique_together = (('turysta', 'wycieczka'),)

    def __str__(self) -> str:
        return f'{str(self.turysta)} ---> {str(self.wycieczka)}'


class UczestnictwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uczestnictwo
        fields = '__all__'
