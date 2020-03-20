from django.contrib import admin
from main.models import Product
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class productAdmin(admin.ModelAdmin):
    #fields = ["productName", "productCost", "productDescription", "datePublished"]
    fieldsets = [ #zauzeto ime u pythonu...
        ("Ime/Cijena", {"fields":["productName", "productCost"]}),
        ("Opis/Datum Objave", {"fields":["productDescription"]}),
        ("Opis/Datum Objave", {"fields": ["datePublished"]})
    ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
    }

admin.site.register(Product, productAdmin)