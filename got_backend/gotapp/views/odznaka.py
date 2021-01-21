from gotapp.models.odznaka import Odznaka, OdznakaSerializer
from rest_framework import generics


class OdznakaList(generics.ListCreateAPIView):
    queryset = Odznaka.objects.all()
    serializer_class = OdznakaSerializer


class OdznakaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odznaka.objects.all()
    serializer_class = OdznakaSerializer


class OdznakaListByKsiazeczka(OdznakaList):
    lookup_field = 'ksiazeczka'
