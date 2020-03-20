from django.shortcuts import render
from main.models import Product

# Create your views here.

def homepage(request):
    templateName = 'main/home.html'
    context = {}
    context['Proizvodi'] = Product.objects.all()
    return render(request, templateName, context)