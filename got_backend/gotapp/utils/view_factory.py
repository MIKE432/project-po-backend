from typing import Tuple
from rest_framework import serializers, generics
from django.db import models


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'


def create_serializer(model: models.Model, fields: Tuple[str, ...]) -> CustomSerializer:
    ser = CustomSerializer
    ser.Meta.fields = fields
    ser.Meta.model = model
    return ser


def get_detail_view(model: models.Model, fields: Tuple[str, ...], read_only=False):
    ser = create_serializer(model, fields)

    if read_only:
        view = generics.RetrieveAPIView
    else:
        view = generics.RetrieveUpdateAPIView

    view.queryset = model.objects.all()
    view.serializer_class = ser
    return view.as_view()
