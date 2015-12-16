from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import *
from django.http import HttpResponse

# Create your views here.
from wyszukiwarka.forms import *


def index(request):
    return render(request, "base.html", {})

def wyszukiwanie(request):
    c={}
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            wyszukiwanie = form.save(commit=False)
            wyszukiwanie.save()
            return redirect("/przegladanie/" + str(wyszukiwanie.id))
    else:
        form=SearchForm()
    c['form']=form
    return render(request, "wyszukiwanie.html", c)


def przegladanie(request, s_id=0):
    c={}
    baseCars = Samochody.objects.all()

    #marka = request.POST.get('Marka')
    #model = request.POST.get('Model')
    #cena_od = request.POST.get('cena_od')
    #cena_do = request.POST.get('cena_do')
    #rocznik_od = request.POST.get('rocznik_od')
    #rocznik_do = request.POST.get('rocznik_do')
    try:
        szukane = Wyszukiwanie.objects.get(id = s_id)
        if szukane.Marka:
            baseCars = baseCars.filter(Marka = szukane.Marka)
        if szukane.Model:
            baseCars = baseCars.filter(Model = szukane.Model)
        if szukane.Cena_od:
            baseCars = baseCars.filter(Cena__gte = szukane.Cena_od)
        if szukane.Cena_do:
            baseCars = baseCars.filter(Cena__lte = szukane.Cena_do)
        if szukane.Rocznik_od:
            baseCars = baseCars.filter(Rocznik__gte = szukane.Rocznik_od)
        if szukane.Rocznik_do:
            baseCars = baseCars.filter(Rocznik__lte = szukane.Rocznik_do)
    except:
        s_id=0

    baseCars = baseCars.order_by('Marka')
    page = request.GET.get('page')
    if not page:
        page=1
    paginator = Paginator(baseCars, 10)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    c['cars']=cars
    c['s_id']=s_id
    return render(request, "przegladanie.html", c)

def szczegoly(request, s_id):
    c={}
    id=request.GET.get('id')
    car = Samochody.objects.get(id=id)
    nadwozia = Nadwozia.objects.all()
    nadwozia = nadwozia.filter(Samochod = car)
    c['car'] = car
    c['s_id'] = s_id
    c['nadwozia'] = nadwozia
    return render(request, "szczegoly.html", c)

def porownanie(request, s_id):
    c={}
    id=request.GET.getlist('cars')
    cars = Samochody.objects.all()
    cars = cars.filter(id__in=id)
    c['cars'] = cars
    c['ids'] = id
    c['s_id']=s_id
    return render(request, "porownanie.html", c)