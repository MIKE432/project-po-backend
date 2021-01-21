from gotapp.models.trasa import Trasa, TrasaSerializer
from rest_framework import generics


class TrasaList(generics.ListCreateAPIView):
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer


class TrasaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer
