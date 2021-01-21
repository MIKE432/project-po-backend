from gotapp.models.grupa_gorska import GrupaGorskaSerializer, GrupaGorska, GrupaGorskaSerializerNested
from rest_framework import generics


class GrupaGorskaList(generics.ListCreateAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializer

class GrupaGorskaListNested(generics.ListAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializerNested


class GrupaGorskaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializer

class GrupaGorskaDetailNested(generics.ListAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializerNested
