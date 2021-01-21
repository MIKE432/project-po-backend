from gotapp.views.mixins import MultipleFieldLookupORMixin
from gotapp.models.uprawnienie import Uprawnienie, UprawnienieSerializer
from rest_framework import generics


class UprawnienieList(generics.ListCreateAPIView):
    queryset = Uprawnienie.objects.all()
    serializer_class = UprawnienieSerializer


class UprawnienieDetail(MultipleFieldLookupORMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Uprawnienie.objects.all()
    serializer_class = UprawnienieSerializer
    lookup_fields = ['legitymacja', 'grupaGorska']
