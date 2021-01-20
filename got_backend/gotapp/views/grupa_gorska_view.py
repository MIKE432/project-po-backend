from gotapp.models.grupa_gorska import GrupaGorskaSerializer, GrupaGorska
from rest_framework import generics


class GrupaGorskaList(generics.ListCreateAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializer


class GrupaGorskaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupaGorska.objects.all()
    serializer_class = GrupaGorskaSerializer
