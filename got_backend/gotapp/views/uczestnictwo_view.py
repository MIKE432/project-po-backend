from gotapp.models.wycieczka import WycieczkaSerializerNested
from gotapp.models.uczestnictwo import Uczestnictwo, UczestnictwoSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class UczestnictwoList(generics.ListCreateAPIView):
    queryset = Uczestnictwo.objects.all()
    serializer_class = UczestnictwoSerializer

    def post(self, request, format=None):
        serializer = UczestnictwoSerializer(data=request.data)
        if serializer.is_valid():
            wycieczka = serializer.validated_data['wycieczka']
            wycieczka_ser = WycieczkaSerializerNested(wycieczka)
            serializer.save()
            return Response(wycieczka_ser.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UczestnictwoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uczestnictwo.objects.all()
    serializer_class = UczestnictwoSerializer
