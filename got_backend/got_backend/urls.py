"""got_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from gotapp.views.trasa_view import TrasaDetail, TrasaDetailNested, TrasaList, TrasaListNested
from gotapp.views.uczestnictwo_view import UczestnictwoDetail, UczestnictwoList
from gotapp.views.wycieczka_view import WycieczkaDetail, WycieczkaDetailNested, WycieczkaList, WycieczkaListNested
from gotapp.views.odznaka import OdznakaDetail, OdznakaList, OdznakaListByKsiazeczka
from gotapp.views.ksiazeczka_view import KsiazeczkaDetail, KsiazeczkaDetailByOwner, KsiazeczkaDetailByOwnerNested, KsiazeczkaDetailNested, KsiazeczkaList
from gotapp.views.stopien_odznaki_view import StopienOdznakiList
from gotapp.views.rodzaj_odznaki_view import RodzajOdznakiList
from gotapp.views.uprawnienie_view import UprawnienieDetail, UprawnienieList
from gotapp.views.legitymacja_view import LegitymacjaList
from gotapp.views.osoba_view import OsobaDetail, OsobaDetailNested, OsobaList, OsobaListNested
from gotapp.views.odcinek_weryfikowany_view import OdcinekWeryfikowanyDetail, OdcinekWeryfikowanyDetailNested, OdcinekWeryfikowanyList, OdcinekWeryfikowanyListNested
from gotapp.views.odcinek_view import OdcinekDetail, OdcinekDetailCzyAktywny, OdcinekDetailNested, OdcinekList, OdcinekListNested
from gotapp.views.punkt_view import PunktDetail, PunktDetailNested, PunktList, PunktListNested
from gotapp.views.grupa_gorska_view import GrupaGorskaDetail, GrupaGorskaDetailNested, GrupaGorskaList, GrupaGorskaListNested
from gotapp.views.region_view import RegionList, RegionDetail
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('regiony/', RegionList.as_view()),
    path('regiony/<int:pk>/', RegionDetail.as_view()),
    path('grupyGorskie/', GrupaGorskaList.as_view()),
    path('grupyGorskie/<str:pk>/', GrupaGorskaDetail.as_view()),
    path('grupyGorskie/details/', GrupaGorskaListNested.as_view()),
    path('grupyGorskie/<str:pk>/details/', GrupaGorskaDetailNested.as_view()),
    path('punkty/', PunktList.as_view()),
    path('punkty/<int:pk>/', PunktDetail.as_view()),
    path('punkty/details/', PunktListNested.as_view()),
    path('punkty/<int:pk>/details/', PunktDetailNested.as_view()),
    path('odcinki/', OdcinekList.as_view()),
    path('odcinki/<int:pk>/', OdcinekDetail.as_view()),
    path('odcinki/details/', OdcinekListNested.as_view()),
    path('odcinki/<int:pk>/details/', OdcinekDetailNested.as_view()),
    path('odcinkiWer/', OdcinekWeryfikowanyList.as_view()),
    path('odcinkiWer/<int:pk>/', OdcinekWeryfikowanyDetail.as_view()),
    path('odcinkiWer/details/', OdcinekWeryfikowanyListNested.as_view()),
    path('odcinkiWer/<int:pk>/details/',
         OdcinekWeryfikowanyDetailNested.as_view()),
    path('osoby/', OsobaList.as_view()),
    path('osoby/<int:pk>/', OsobaDetail.as_view()),
    path('osoby/details/', OsobaListNested.as_view()),
    path('osoby/<int:pk>/details/', OsobaDetailNested.as_view()),
    path('legitymacje/', LegitymacjaList.as_view()),
    path('uprawnienia/', UprawnienieList.as_view()),
    path('uprawnienia/<int:legitymacja>/<str:grupaGorska>/',
         UprawnienieDetail.as_view()),
    path('rodzajeOdznak/', RodzajOdznakiList.as_view()),
    path('stopnieOdznak/', StopienOdznakiList.as_view()),
    path('ksiazeczki/', KsiazeczkaList.as_view()),
    path('ksiazeczki/<int:pk>/', KsiazeczkaDetail.as_view()),
    path('ksiazeczki/byowner/<int:turysta>/',
         KsiazeczkaDetailByOwner.as_view()),
    path('ksiazeczki/<int:pk>/details/', KsiazeczkaDetailNested.as_view()),
    path('ksiazeczki/byowner/<int:turysta>/details/',
         KsiazeczkaDetailByOwnerNested.as_view()),
    path('odznaki/', OdznakaList.as_view()),
    path('odznaki/<int:pk>/', OdznakaDetail.as_view()),
    path('odznaki/byksiazeczka/<int:ksiazeczka>/',
         OdznakaListByKsiazeczka.as_view()),
    path('wycieczki/', WycieczkaList.as_view()),
    path('wycieczki/details/', WycieczkaListNested.as_view()),
    path('wycieczki/<int:pk>/', WycieczkaDetail.as_view()),
    path('wycieczki/<int:pk>/details/', WycieczkaDetailNested.as_view()),
    path('uczestnictwa/', UczestnictwoList.as_view()),
    path('uczestnictwa/<int:pk>/', UczestnictwoDetail.as_view()),
    path('trasy/', TrasaList.as_view()),
    path('trasy/<int:pk>/', TrasaDetail.as_view()),
    path('trasy/details/', TrasaListNested.as_view()),
    path('trasy/<int:pk>/details/', TrasaDetailNested.as_view()),
    path('odcinki/<int:pk>/czyAktywny/', OdcinekDetailCzyAktywny.as_view()),
]
