from django.db import models

# Create your models here.

class Produkt(models.Model):
    nazwa = models.CharField(max_length=120)
    opis = models.TextField(blank=True, null=True)
    silnik = models.CharField(blank=True, null=True, max_length=120)
    skrzynia = models.TextField(blank=True, null=True, default='Manualna')
    kolor = models.CharField(blank=True, null=True, max_length=120)
    drzwi = models.DecimalField(blank=True, null=True, max_digits=1, decimal_places=0)
    cena = models.DecimalField(max_digits=1000000, decimal_places=2)

