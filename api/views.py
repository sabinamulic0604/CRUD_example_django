from rest_framework import generics

from .models import Proizvod, Lokacija
from .serializers import ProizvodSerializer, LokacijaSerializer

class ProizvodLista(generics.ListCreateAPIView):
    serializer_class = ProizvodSerializer

    def get_queryset(self):
        queryset = Proizvod.objects.all()
        lokacija = self.request.query_params.get('lokacija')
        if lokacija is not None:
            queryset=queryset.filter(lokacijaProizvoda=lokacija)
        return queryset


class ProizvodOsobine (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProizvodSerializer
    queryset = Proizvod.objects.all()


class LokacijaLista (generics.ListCreateAPIView):
    serializer_class = LokacijaSerializer
    queryset = Lokacija.objects.all()

class LokacijaOsobine (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LokacijaSerializer
    queryset = Lokacija.objects.all()    

