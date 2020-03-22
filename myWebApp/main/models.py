from django.db import models

# Create your models here.

class Proizvod(models.Model):
    vrsta = models.CharField(max_length=200)
    ime = models.CharField(max_length=200)
    proizvodjac = models.CharField(max_length=200, default="nema")
    trgovina = models.CharField(max_length=200)
    cijena = models.FloatField()

    def __str__(self):
        return self.ime

