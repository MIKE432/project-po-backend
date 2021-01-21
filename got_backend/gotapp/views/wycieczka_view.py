from gotapp.models.wycieczka import Wycieczka, WycieczkaSerializer
from rest_framework import generics


class WycieczkaList(generics.ListCreateAPIView):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializer


class WycieczkaDetail( generics.RetrieveUpdateDestroyAPIView):
    queryset = Wycieczka.objects.all()
    serializer_class = WycieczkaSerializer
