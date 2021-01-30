from gotapp.models.odznaka import Odznaka, OdznakaSerializer, OdznakaSerializerNested
from rest_framework import generics


class OdznakaList(generics.ListCreateAPIView):
    queryset = Odznaka.objects.all()
    serializer_class = OdznakaSerializer


class OdznakaListNested(OdznakaList):
    serializer_class = OdznakaSerializerNested

class OdznakaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odznaka.objects.all()
    serializer_class = OdznakaSerializer


class OdznakaListByKsiazeczka(OdznakaListNested):
    lookup_field = 'ksiazeczka'
