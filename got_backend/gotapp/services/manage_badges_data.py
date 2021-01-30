from gotapp.models import ksiazeczka
from gotapp.models.odznaka import OdznakaSerializer
from gotapp.models.wycieczka import WycieczkaSerializerNested
from gotapp.models.osoba import OsobaSerializerNested
from typing import Any, Dict, List
from django.db.models.base import Model
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from gotapp.models import Osoba, Ksiazeczka, Wycieczka, Odznaka, StopienOdznaki, RodzajOdznaki
from gotapp.models.ksiazeczka import KsiazeczkaSerializerNested
import datetime as dt
from rest_framework import status
from django.db.models import Q


TYPE_POPULARNA = 1
TYPE_WGORY = 2
TYPE_MALA = 3
TYPE_DUZA = 4
TYPE_WYTRWALOSC = 5

LEVEL_BRAZOWA = 1
LEVEL_SREBRNA = 2
LEVEL_ZLOTA = 3
LEVEL_MALA = 4
LEVEL_DUZA = 5


class ManageBadgesData(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.response_data: Dict[str, Any] = {}

    def get_object(self, model: Model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get_ksiazeczka(self, osoba_id) -> Ksiazeczka:
        try:
            return Ksiazeczka.objects.get(turysta_id=osoba_id)
        except Ksiazeczka.DoesNotExist:
            raise Http404

    def get_odznaki(self, ksiazeczka: Ksiazeczka):
        k_ser = KsiazeczkaSerializerNested(ksiazeczka)
        return k_ser.data['odznaki']

    def get_wycieczki(self, osoba: Osoba):
        o_ser = OsobaSerializerNested(osoba)
        wycieczki = Wycieczka.objects.filter(pk__in=o_ser.data['wycieczki'])
        w_data = WycieczkaSerializerNested(wycieczki, many=True).data
        for w in w_data:
            w['uczestnicy'] = []
        return w_data

    def get_response_data(self, pk):
        response_data: Dict[str, Any] = {}
        ksiazeczka: Ksiazeczka = self.get_ksiazeczka(pk)
        avPoints = ksiazeczka.punktacja - self.calculate_used_points(pk)
        if avPoints < 0:
            avPoints = 0
        response_data['availablePoints'] = avPoints
        response_data['punktacja'] = ksiazeczka.punktacja
        response_data['odznaki'] = self.create_badges(pk)
        response_data['ksiazeczka'] = ksiazeczka.id
        return response_data

    def calculate_used_points(self, pk):
        ksiazeczka = self.get_ksiazeczka(pk)
        points_sum = 0
        odznakiPrzyznane = Odznaka.objects.filter(Q(ksiazeczka=ksiazeczka.id) & (
            Q(dataPrzyznania__year=dt.date.today().year) | Q(czyRozp=True)))
        for odznaka in odznakiPrzyznane:
            points_sum += odznaka.wyPkt

        return points_sum

    def create_badges(self, pk):
        available_badges: List[Odznaka] = []
        ksiazeczka = self.get_ksiazeczka(pk)
        odznakiPrzyznane = Odznaka.objects.filter(Q(ksiazeczka=ksiazeczka.id) & (
            Q(dataPrzyznania__year=dt.date.today().year) | Q(czyRozp=True)))
        ignored_types = set([(op.rodzaj.id, op.stopien.id)
                             for op in odznakiPrzyznane])

        if not (TYPE_POPULARNA, LEVEL_BRAZOWA) in ignored_types:
            odznaka = Odznaka(wyPkt=60, stopien=StopienOdznaki(pk=LEVEL_BRAZOWA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_POPULARNA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_MALA, LEVEL_BRAZOWA) in ignored_types:
            odznaka = Odznaka(wyPkt=120, stopien=StopienOdznaki(pk=LEVEL_BRAZOWA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_MALA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_MALA, LEVEL_SREBRNA) in ignored_types:
            odznaka = Odznaka(wyPkt=360, stopien=StopienOdznaki(pk=LEVEL_SREBRNA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_MALA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_MALA, LEVEL_ZLOTA) in ignored_types:
            odznaka = Odznaka(wyPkt=720, stopien=StopienOdznaki(pk=LEVEL_ZLOTA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_MALA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_DUZA, LEVEL_BRAZOWA) in ignored_types:
            odznaka = Odznaka(wyPkt=800, stopien=StopienOdznaki(pk=LEVEL_BRAZOWA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_DUZA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_DUZA, LEVEL_SREBRNA) in ignored_types:
            odznaka = Odznaka(wyPkt=900, stopien=StopienOdznaki(pk=LEVEL_SREBRNA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_DUZA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        if not (TYPE_DUZA, LEVEL_ZLOTA) in ignored_types:
            odznaka = Odznaka(wyPkt=1000, stopien=StopienOdznaki(pk=LEVEL_ZLOTA, stopien=""),
                              rodzaj=RodzajOdznaki(pk=TYPE_DUZA, rodzaj=""), ksiazeczka=ksiazeczka)
            available_badges.append(odznaka)

        o_ser = OdznakaSerializer(available_badges, many=True)
        return o_ser.data

    def get(self, request, pk, format=None):
        self.response_data = self.get_response_data(pk)
        return Response(self.response_data)

    def post(self, request, pk, format=None):
        serializer = OdznakaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ksiazeczka: Ksiazeczka = Ksiazeczka.objects.get(
                pk=int(request.data['ksiazeczka']))
            return Response(self.get_response_data(ksiazeczka.turysta), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
