from gotapp.models.punkt import Punkt
from gotapp.utils.view_factory import create_serializer
from gotapp.models.odcinek import Odcinek, OdcinekSerializer, OdcinekSerializerCzyAktywny, OdcinekSerializerNested
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
import mpu


def without_keys(d, keys):
    return {k: v for k, v in d.items() if k not in keys}


class OdcinekList(generics.ListCreateAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializer

    def post(self, request, format=None):
        req_data = {x: request.POST.get(
            x) for x in request.POST.keys() if request.POST.get(x) != ''}

        poczatek: Punkt = Punkt.objects.get(pk=int(req_data['poczatek']))
        koniec: Punkt = Punkt.objects.get(pk=int(req_data['koniec']))

        if not 'przewyzszenie' in req_data:
            przewyzszenie = koniec.wysokosc - poczatek.wysokosc
            req_data['przewyzszenie'] = przewyzszenie

        if not 'dlugosc' in req_data:
            loc1 = (poczatek.szerokoscGeo, poczatek.dlugoscGeo)
            loc2 = (koniec.szerokoscGeo, koniec.dlugoscGeo)
            dlugosc = mpu.haversine_distance(loc1, loc2) * 1000
            req_data['dlugosc'] = dlugosc

        serializer = OdcinekSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OdcinekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializer


class OdcinekListNested(generics.ListAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializerNested


class OdcinekDetailNested(generics.RetrieveAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializerNested


class OdcinekDetailCzyAktywny(generics.RetrieveUpdateAPIView):
    queryset = Odcinek.objects.all()
    serializer_class = OdcinekSerializerCzyAktywny

    def get_object(self, pk):
        try:
            return Odcinek.objects.get(pk=pk)
        except Odcinek.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        odcinek = self.get_object(pk)
        serializer = OdcinekSerializerCzyAktywny(odcinek)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        odcinek = self.get_object(pk)
        serializer = OdcinekSerializerCzyAktywny(odcinek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result_ser = OdcinekSerializer(odcinek)
            return Response(result_ser.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
