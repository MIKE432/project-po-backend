from gotapp.models.odcinek import Odcinek, OdcinekSerializer, OdcinekSerializerNested
from rest_framework import generics


class OdcinekList(generics.ListCreateAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializer


class OdcinekListNested(generics.ListAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializerNested


class OdcinekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializer


class OdcinekDetailNested(generics.RetrieveAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializerNested
