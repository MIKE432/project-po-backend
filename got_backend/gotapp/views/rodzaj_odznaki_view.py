from gotapp.models.rodzaj_odznaki import RodzajOdznaki, RodzajOdznakiSerializer
from rest_framework import generics


class RodzajOdznakiList(generics.ListCreateAPIView):
    queryset = RodzajOdznaki.objects.all()
    serializer_class = RodzajOdznakiSerializer
