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

def results(request):
    context = {}
    ime_templatea = "main/results.html"

    ime_artikla = ""
    vrsta_artikla = ""
    proizvodjac = ""
    trgovina_artikla = ""
    minimalna_cijena = 0
    maksimalna_cijena = 0

    if request.method == 'POST':
        ime_artikla = str(request.POST['ime_artikla']).lower()
        vrsta_artikla = str(request.POST['vrsta_artikla']).lower()
        proizvodjac = str(request.POST['proizvodjac_artikla']).lower()
        trgovina_artikla = str(request.POST['trgovina_artikla']).lower()
        minimalna_cijena = float(request.POST['minimalna_cijena'])
        maksimalna_cijena = float(request.POST['maksimalna_cijena'])

        #pretraga....

        querySet = Proizvod.objects.filter(cijena__lte=maksimalna_cijena)
        querySet = querySet.filter(cijena__gte=minimalna_cijena)

        if ime_artikla != "":
            querySet = querySet.filter(ime__contains=ime_artikla)

        if vrsta_artikla != "":
            querySet = querySet.filter(vrsta__contains=vrsta_artikla)

        if proizvodjac != "":
            querySet = querySet.filter(proizvodjac__contains=proizvodjac)

        if trgovina_artikla != "":
            querySet = querySet.filter(trgovina__contains=trgovina_artikla)

        if querySet:
            context['proizvodi'] = querySet
        else:
            context['proizvodi'] = "nema_artikala"
    else:
        ime_templatea = "main/zabrana.html"

    return render(request, ime_templatea, context)



