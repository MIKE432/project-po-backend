from gotapp.models.stopien_odznaki import StopienOdznaki, StopienOdznakiSerializer
from rest_framework import generics


class StopienOdznakiList(generics.ListCreateAPIView):
    queryset = StopienOdznaki.objects.all()
    serializer_class = StopienOdznakiSerializer
