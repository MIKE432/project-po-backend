from gotapp.models.trasa import TrasaSerializer, TrasaSerializerNested
from gotapp.models.osoba import Osoba, OsobaSerializer, OsobaSerializerNested
from gotapp.models.wycieczka import WycieczkaSerializer
from gotapp.models.odcinek import OdcinekSerializer
from rest_framework import generics



class TrasaSerializerCustom(TrasaSerializer):
    odcinki = OdcinekSerializer(read_only=True, many=True)

class WycieczkaSerializerCustom(WycieczkaSerializer):
    trasa = TrasaSerializerCustom(read_only=True)

class OsobaSerializerCustom(OsobaSerializerNested):
    wycieczki = WycieczkaSerializerCustom(read_only=True, many=True)

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
