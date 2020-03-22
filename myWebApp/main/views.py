from django.shortcuts import render, redirect
from main.models import Proizvod

# Create your views here.

def homepage(request):
    ime_templatea = 'main/home.html'
    context = {}
    return render(request, ime_templatea, context)
def search(request):
    context = {}
    ime_templatea = "main/search.html"
    return render(request, ime_templatea, context)

def post(request):
    poruka = ""
    ime_templatea = "main/post.html"

    if request.method == "POST":
        ime_artikla = str(request.POST['ime_artikla']).lower()
        vrsta_artikla = str(request.POST['vrsta_artikla']).lower()
        proizvodjac = str(request.POST['proizvodjac_artikla']).lower()
        cijena_artikla = float(request.POST['cijena_artikla'])
        trgovina_artikla = str(request.POST['trgovina_artikla']).lower()

        querySet = Proizvod.objects.filter(vrsta=vrsta_artikla)
        querySet = querySet.filter(ime=ime_artikla)
        querySet = querySet.filter(proizvodjac=proizvodjac)
        if querySet:
            poruka = "stari_artikal"
            proizvod = querySet[0]

            if proizvod.cijena > cijena_artikla:
                proizvod.cijena = cijena_artikla
                proizvod.trgovina = trgovina_artikla
                proizvod.save()
        else:
            poruka = "novi_artikal"
            proizvod = Proizvod(ime=ime_artikla, vrsta=vrsta_artikla, proizvodjac=proizvodjac, cijena=cijena_artikla, trgovina=trgovina_artikla)
            proizvod.save()
    else:
        poruka = ""

    context = {"poruka" : poruka}
    return render(request, ime_templatea, context)

def about(request):
    context = {}
    ime_templatea = "main/about.html"
    return render(request, ime_templatea, context)