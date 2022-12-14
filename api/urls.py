from django.urls import path
from .views import ProizvodLista, ProizvodOsobine, LokacijaOsobine, LokacijaLista

urlpatterns = [
    path('lokacija/', LokacijaLista.as_view()),
    path('lokacija/<int:pk>/', LokacijaOsobine.as_view()),
    path('proizvod/', ProizvodLista.as_view()),
    path('proizvod/<int:pk>/', ProizvodOsobine.as_view()),
]