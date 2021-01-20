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
from gotapp.views.grupa_gorska_view import GrupaGorskaDetail, GrupaGorskaList
from rest_framework.urlpatterns import format_suffix_patterns
from gotapp.views import region_view
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('regiony/', region_view.RegionList.as_view()),
    path('regiony/<int:pk>', region_view.RegionDetail.as_view()),
    path('grupyGorskie/', GrupaGorskaList.as_view()),
    path('grupyGorskie/<str:pk>', GrupaGorskaDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
