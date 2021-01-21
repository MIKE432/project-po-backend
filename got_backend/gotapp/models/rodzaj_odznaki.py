from django.db import models
from rest_framework import serializers


class RodzajOdznaki(models.Model):
    rodzaj = models.CharField(max_length=40)

    class Meta:
        ordering = ['rodzaj']

    def __str__(self):
        return self.rodzaj


class RodzajOdznakiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RodzajOdznaki
        fields = '__all__'
