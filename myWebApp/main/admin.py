from django.contrib import admin
from main.models import Proizvod
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class productAdmin(admin.ModelAdmin):
    #fields = ["productName", "productCost", "productDescription", "datePublished"]
    fieldsets = [ #zauzeto ime u pythonu...
        ("Ime/Vrsta proizvoda :", {"fields":["ime", "vrsta"]}),
        ("Cijena/Trgovina :", {"fields":["cijena", "trgovina"]}),
        ("Proizvođač :", {"fields":["proizvodjac"]})
    ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
    }

admin.site.register(Proizvod, productAdmin)