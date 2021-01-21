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
from gotapp.views.odznaka import OdznakaDetail, OdznakaList, OdznakaListByKsiazeczka
from gotapp.views.ksiazeczka_view import KsiazeczkaDetail, KsiazeczkaDetailByOwner, KsiazeczkaDetailByOwnerNested, KsiazeczkaDetailNested, KsiazeczkaList
from gotapp.views.stopien_odznaki_view import StopienOdznakiList
from gotapp.views.rodzaj_odznaki_view import RodzajOdznakiList
from gotapp.views.uprawnienie_view import UprawnienieDetail, UprawnienieList
from gotapp.views.legitymacja_view import LegitymacjaList
from gotapp.views.osoba_view import OsobaDetail, OsobaDetailNested, OsobaList, OsobaListNested
from gotapp.views.odcinek_weryfikowany_view import OdcinekWeryfikowanyDetail, OdcinekWeryfikowanyDetailNested, OdcinekWeryfikowanyList, OdcinekWeryfikowanyListNested
from gotapp.views.odcinek_view import OdcinekDetail, OdcinekDetailNested, OdcinekList, OdcinekListNested
from gotapp.views.punkt_view import PunktDetail, PunktDetailNested, PunktList, PunktListNested
from gotapp.views.grupa_gorska_view import GrupaGorskaDetail, GrupaGorskaDetailNested, GrupaGorskaList, GrupaGorskaListNested
from rest_framework.urlpatterns import format_suffix_patterns
from gotapp.views.region_view import RegionList, RegionDetail
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('regiony/', RegionList.as_view()),
    path('regiony/<int:pk>', RegionDetail.as_view()),
    path('grupyGorskie/', GrupaGorskaList.as_view()),
    path('grupyGorskie/<str:pk>', GrupaGorskaDetail.as_view()),
    path('grupyGorskieNested/', GrupaGorskaListNested.as_view()),
    path('grupyGorskieNested/<str:pk>', GrupaGorskaDetailNested.as_view()),
    path('punkty/', PunktList.as_view()),
    path('punkty/<int:pk>', PunktDetail.as_view()),
    path('punktyNested/', PunktListNested.as_view()),
    path('punktyNested/<int:pk>', PunktDetailNested.as_view()),
    path('odcinki/', OdcinekList.as_view()),
    path('odcinki/<int:pk>', OdcinekDetail.as_view()),
    path('odcinkiNested/', OdcinekListNested.as_view()),
    path('odcinkiNested/<int:pk>', OdcinekDetailNested.as_view()),
    path('odcinkiWer/', OdcinekWeryfikowanyList.as_view()),
    path('odcinkiWer/<int:pk>', OdcinekWeryfikowanyDetail.as_view()),
    path('odcinkiWerNested/', OdcinekWeryfikowanyListNested.as_view()),
    path('odcinkiWerNested/<int:pk>', OdcinekWeryfikowanyDetailNested.as_view()),
    path('osoby/', OsobaList.as_view()),
    path('osoby/<int:pk>', OsobaDetail.as_view()),
    path('osobyNested/', OsobaListNested.as_view()),
    path('osobyNested/<int:pk>', OsobaDetailNested.as_view()),
    path('legitymacje/', LegitymacjaList.as_view()),
    path('uprawnienia/', UprawnienieList.as_view()),
    path('uprawnienia/<int:legitymacja>/<str:grupaGorska>',
         UprawnienieDetail.as_view()),
    path('rodzajeOdznak/', RodzajOdznakiList.as_view()),
    path('stopnieOdznak/', StopienOdznakiList.as_view()),
    path('ksiazeczki/', KsiazeczkaList.as_view()),
    path('ksiazeczki/<int:pk>', KsiazeczkaDetail.as_view()),
    path('ksiazeczki/owner/<int:turysta>', KsiazeczkaDetailByOwner.as_view()),
    path('ksiazeczkiNested/<int:pk>', KsiazeczkaDetailNested.as_view()),
    path('ksiazeczkiNested/owner/<int:turysta>',
         KsiazeczkaDetailByOwnerNested.as_view()),
    path('odznaki/', OdznakaList.as_view()),
    path('odznaki/<int:pk>', OdznakaDetail.as_view()),
    path('odznaki/ksiazeczka/<int:ksiazeczka>',
         OdznakaListByKsiazeczka.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
