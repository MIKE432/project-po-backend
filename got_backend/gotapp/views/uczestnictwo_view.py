from gotapp.models.uczestnictwo import Uczestnictwo, UczestnictwoSerializer
from rest_framework import generics


class UczestnictwoList(generics.ListCreateAPIView):
    queryset = Uczestnictwo.objects.all()
    serializer_class = UczestnictwoSerializer


class UczestnictwoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uczestnictwo.objects.all()
    serializer_class = UczestnictwoSerializer
