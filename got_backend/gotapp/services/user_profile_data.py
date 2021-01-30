from gotapp.models.wycieczka import WycieczkaSerializerNested
from gotapp.models.osoba import OsobaSerializerNested
from typing import Any, Dict
from django.db.models.base import Model
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from gotapp.models import Osoba, Ksiazeczka, Wycieczka
from gotapp.models.ksiazeczka import KsiazeczkaSerializerNested


class UserProfileView(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.response_data: Dict[str, Any] = {}

    def get_object(self, model: Model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get_ksiazeczka(self, osoba_id):
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

    def get(self, request, pk, format=None):
        osoba: Osoba = self.get_object(Osoba, pk)
        self.response_data['imie'] = osoba.imie
        self.response_data['nazwisko'] = osoba.nazwisko

        ksiazeczka: Ksiazeczka = self.get_ksiazeczka(pk)
        self.response_data['punktacja'] = ksiazeczka.punktacja
        self.response_data['odznaki'] = self.get_odznaki(ksiazeczka)
        self.response_data['ksiazeczka'] = ksiazeczka.id
        self.response_data['wycieczki'] = self.get_wycieczki(osoba)

        return Response(self.response_data)
