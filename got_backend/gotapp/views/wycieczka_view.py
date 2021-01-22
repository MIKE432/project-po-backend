from gotapp.models.wycieczka import Wycieczka, WycieczkaSerializer, WycieczkaSerializerNested
from rest_framework import generics


class WycieczkaList(generics.ListCreateAPIView):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializer


class WycieczkaListNested(WycieczkaList):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializerNested


class WycieczkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializer


class WycieczkaDetailNested(generics.RetrieveAPIView):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializerNested
