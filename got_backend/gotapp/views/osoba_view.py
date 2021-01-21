from gotapp.models.osoba import Osoba, OsobaSerializer, OsobaSerializerNested
from rest_framework import generics


class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class OsobaListNested(generics.ListAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializerNested


class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class OsobaDetailNested(generics.RetrieveAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializerNested
