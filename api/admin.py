from django.contrib import admin

from .models import Proizvod, Lokacija

#nakon reg admin vidi oba modela
admin.site.register(Proizvod)
admin.site.register(Lokacija)