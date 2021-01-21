from django.db import models
from rest_framework import serializers


class StopienOdznaki(models.Model):
    stopien = models.CharField(max_length=40)

    class Meta:
        ordering = ['stopien']

    def __str__(self) -> str:
        return self.stopien


class StopienOdznakiSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopienOdznaki
        fields = '__all__'
