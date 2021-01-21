from gotapp.models.odcinek_weryfikowany import OdcinekWeryfikowany, OdcinekWeryfikowanySerializer, OdcinekWeryfikowanySerializerNested
from rest_framework import generics


class OdcinekWeryfikowanyList(generics.ListCreateAPIView):
    queryset = OdcinekWeryfikowany.objects.all()
    serializer_class = OdcinekWeryfikowanySerializer


class OdcinekWeryfikowanyListNested(generics.ListAPIView):
    queryset = OdcinekWeryfikowany.objects.all()
    serializer_class = OdcinekWeryfikowanySerializerNested


class OdcinekWeryfikowanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OdcinekWeryfikowany.objects.all()
    serializer_class = OdcinekWeryfikowanySerializer


class OdcinekWeryfikowanyDetailNested(generics.RetrieveAPIView):
    queryset = OdcinekWeryfikowany.objects.all()
    serializer_class = OdcinekWeryfikowanySerializerNested
