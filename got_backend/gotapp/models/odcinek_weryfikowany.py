from gotapp.models.odcinek import OdcinekSerializerNested
from gotapp.models.osoba import OsobaSerializerNested
from django.db import models
from rest_framework import serializers


class OdcinekWeryfikowany(models.Model):
    dataWer = models.DateField(blank=True, null=True)
    czyZwer = models.BooleanField(blank=True, null=True)
    nrPorz = models.IntegerField()
    odcinek = models.ForeignKey(
        'gotapp.Odcinek', on_delete=models.CASCADE, related_name='odcinki')
    przod = models.ForeignKey('gotapp.Osoba', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['nrPorz']


class OdcinekWeryfikowanySerializer(serializers.ModelSerializer):
    class Meta:
        model = OdcinekWeryfikowany
        fields = '__all__'


class OdcinekWeryfikowanySerializerNested(OdcinekWeryfikowanySerializer):
    odcinek = OdcinekSerializerNested(read_only=True)
    przod = OsobaSerializerNested(read_only=True)
