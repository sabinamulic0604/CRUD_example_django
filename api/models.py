from django.db import models

class Lokacija(models.Model):
    lokacijaName=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.lokacijaName



class Proizvod(models.Model):
    proizvodName=models.CharField(max_length=100)
    datum_dodavanja=models.DateField(auto_now_add=True)
    lokacijaProizvoda=models.ForeignKey(Lokacija, on_delete=models.CASCADE) #kad se obrise lokacija obrisat ce se svi proizvodi na toj lokaciji


    def __str__(self):
        return self.proizvodName

