from django.urls import path
from .views import Proizvod1,  LokacijaLista, ProizvodLista, Lokacija1

urlpatterns = [
    path('lokacije/', LokacijaLista.as_view()),
    path('lokacija/<int:pk>/', Lokacija1.as_view()),
    path('proizvodi/', ProizvodLista.as_view()),
    path('proizvod/<int:pk>/', Proizvod1.as_view()),


]