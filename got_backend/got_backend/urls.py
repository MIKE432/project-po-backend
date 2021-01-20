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
    path('odcinkiNested/<int:pk>', OdcinekDetailNested.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
