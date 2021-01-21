from gotapp.models.legitymacja import Legitymacja, LegitymacjaSerializer
from rest_framework import generics

class LegitymacjaList(generics.ListCreateAPIView):
    queryset = Legitymacja.objects.all()
    serializer_class = LegitymacjaSerializer
