from django.shortcuts import render

from django.http import HttpResponse

from models import *

# Create your views here.

def index(request):
    return render(request, "base.html", {})

def wyszukiwanie(request):
    return render(request, "wyszukiwanie.html", {})

def przegladanie(request):
    c={}
    cars = Samochody.objects.all().order_by('Marka')
    c['cars']=cars
    return render(request, "przegladanie.html", c)