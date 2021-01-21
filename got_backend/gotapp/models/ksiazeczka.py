from gotapp.models.odznaka import OdznakaSerializer
from django.db import models
from rest_framework import serializers


class Ksiazeczka(models.Model):
    punktacja = models.IntegerField()
    turysta = models.OneToOneField(
        'gotapp.Osoba', on_delete=models.CASCADE, related_name='ksiazeczka')

    def __str__(self):
        return self.turysta.__str__()


class KsiazeczkaSerializer(serializers.ModelSerializer):
    odznaki = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Ksiazeczka
        fields = '__all__'


class KsiazeczkaSerializerNested(KsiazeczkaSerializer):
    odznaki = OdznakaSerializer(many=True, read_only=True)
