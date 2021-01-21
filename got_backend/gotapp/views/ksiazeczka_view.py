from gotapp.models.ksiazeczka import Ksiazeczka, KsiazeczkaSerializer, KsiazeczkaSerializerNested
from rest_framework import generics


class KsiazeczkaList(generics.ListCreateAPIView):
    queryset = Ksiazeczka.objects.all()
    serializer_class = KsiazeczkaSerializer


class KsiazeczkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazeczka.objects.all()
    serializer_class = KsiazeczkaSerializer


class KsiazeczkaDetailByOwner(KsiazeczkaDetail):
    lookup_field = 'turysta'


class KsiazeczkaDetailNested(KsiazeczkaDetail):
    serializer_class = KsiazeczkaSerializerNested


class KsiazeczkaDetailByOwnerNested(KsiazeczkaDetailByOwner):
    serializer_class = KsiazeczkaSerializerNested
