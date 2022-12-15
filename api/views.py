from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Proizvod, Lokacija
from .serializers import ProizvodSerializer, LokacijaSerializer

class ProizvodLista(APIView):  #svi proizvodi ili add novi proizvod

    def get(self, request, format=None):
        proizvodi = Proizvod.objects.all()
        serializer = ProizvodSerializer(proizvodi, many=True)                      
        return Response (serializer.data)

    def post (self, request, format=None):
        serializer = ProizvodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LokacijaLista(APIView):  #sve lokacija ili add novu lokaciju

    def get(self, request, format=None):
        lokacije = Lokacija.objects.all()
        serializer = LokacijaSerializer(lokacije, many=True)
        return Response (serializer.data)

    def post (self, request, format=None):
        serializer = LokacijaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Proizvod1(APIView):  #Pregled proizvoda po id-u, update ili brisanje
    
    def get_object(self, pk):
        try:
            return Proizvod.objects.get(pk=pk)
        except Proizvod.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Proizvod = self.get_object(pk)
        serializer = ProizvodSerializer(Proizvod)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Proizvod = self.get_object(pk)
        serializer = ProizvodSerializer(Proizvod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Proizvod = self.get_object(pk)
        Proizvod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class Lokacija1(APIView):  #Pregled lokacija po id-u, update ili brisanje
    
    def get_object(self, pk):
        try:
            return Lokacija.objects.get(pk=pk)
        except Lokacija.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Proizvod = self.get_object(pk)
        serializer = LokacijaSerializer(Proizvod)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Lokacija = self.get_object(pk)
        serializer = LokacijaSerializer(Lokacija, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Lokacija = self.get_object(pk)
        Lokacija.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

