from gotapp.models.trasa import Trasa, TrasaSerializer, TrasaSerializerNested
from rest_framework import generics


class TrasaList(generics.ListCreateAPIView):
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer


class TrasaListNested(TrasaList):
    serializer_class = TrasaSerializerNested


class TrasaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer


class TrasaDetailNested(TrasaDetail):
    serializer_class = TrasaSerializerNested
