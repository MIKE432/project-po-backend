from gotapp.models.punkt import Punkt, PunktSerializer, PunktSerializerNested
from rest_framework import generics


class PunktList(generics.ListCreateAPIView):
    queryset = Punkt.objects.all()
    serializer_class = PunktSerializer


class PunktListNested(generics.ListAPIView):
    queryset = Punkt.objects.all()
    serializer_class = PunktSerializerNested


class PunktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Punkt.objects.all()
    serializer_class = PunktSerializer


class PunktDetailNested(generics.RetrieveAPIView):
    queryset = Punkt.objects.all()
    serializer_class = PunktSerializerNested
