from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

from models import *
from django.http import HttpResponse

# Create your views here.
from wyszukiwarka.forms import *
from base64 import b64encode
from django.core.exceptions import ObjectDoesNotExist
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
    if s_id != '0':
        try:
            szukane = Wyszukiwanie.objects.get(id=s_id)
            if szukane.Marka:
                marki = Marki.objects.get(Marka=szukane.Marka)
                baseCars = baseCars.filter(Marka=marki.id)
            if szukane.Model:
                baseCars = baseCars.filter(Model=szukane.Model)
            if szukane.Cena_od:
                baseCars = baseCars.filter(Cena__gte=szukane.Cena_od)
            if szukane.Cena_do:
                baseCars = baseCars.filter(Cena__lte=szukane.Cena_do)
            if szukane.Rocznik_od:
                baseCars = baseCars.filter(Rocznik__gte=szukane.Rocznik_od)
            if szukane.Rocznik_do:
                baseCars = baseCars.filter(Rocznik__lte=szukane.Rocznik_do)
        except ObjectDoesNotExist:
            pass
            return redirect("/przegladanie/0/")

    baseCars = baseCars.order_by('Marka')
    page = request.GET.get('page')
    if not page:
        page=1
    paginator = Paginator(baseCars, 10)
    try:
        cars = paginator.page(page)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    c['cars']=cars
    c['s_id']=s_id
    return render(request, "przegladanie.html", c)

def model(request, s_id, c_id):
    c={}
    car = Samochody.objects.get(id=c_id)
    nadwozia = Nadwozia.objects.all()
    nadwozia = nadwozia.filter(Samochod = car)
    c['car'] = car
    c['s_id'] = s_id
    c['cenaMax'] = car.Cena + (maxPrice.objects.raw("call samochodMaxPrice(" + c_id + ");"))[0].Cena
    c['nadwozia'] = nadwozia
    c['nadwoziaMax'] = list(maxPrice.objects.raw("call nadwozieMaxPrice(" + c_id + ");"))
    print(c['nadwoziaMax'])
    return render(request, "model.html", c)

def nadwozie(request, s_id, c_id, n_id):
    c={}
    car = Samochody.objects.get(id=c_id)
    nadwozie = Nadwozia.objects.get(id=n_id)
    silniki = Silniki.objects.all()
    silniki = silniki.filter(parametry__Nadwozie = nadwozie)
    parametry = Silniki_Nadwozia.objects.all()
    parametry = parametry.filter(Nadwozie = nadwozie)
    benzynowe = silniki.filter(Paliwo = 'B')
    diesla = silniki.filter(Paliwo = 'D')
    files = Zdjecia.objects.all()
    files = files.filter(Nadwozie = nadwozie)
    for f in files:
        f.Plik = b64encode(f.Plik)
    cenaMax = parametry.aggregate(Max('Oplata'))['Oplata__max']
    c['cenaMax'] = cenaMax
    c['files'] = files
    c['car'] = car
    c['s_id'] = s_id
    c['nadwozie'] = nadwozie
    c['benzynowe'] = benzynowe
    c['diesla'] = diesla
    c['parametry'] = parametry
    return render(request, "nadwozie.html", c)

def silnik(request, s_id, c_id, n_id, e_id):
    c={}
    car = Samochody.objects.get(id = c_id)
    nadwozie = Nadwozia.objects.get(id = n_id)
    silnik = Silniki.objects.get(id = e_id)
    parametry = Silniki_Nadwozia.objects.all()
    parametry = parametry.filter(Nadwozie = nadwozie)
    parametry = parametry.filter(Silnik = silnik)
    c['car'] = car
    c['s_id'] = s_id
    c['nadwozie'] = nadwozie
    c['silnik'] = silnik
    c['parametry'] = parametry[0]
    return render(request, "silnik.html", c)

def porownanie(request, s_id):
    c={}
    id=request.GET.getlist('cars')
    cars = Samochody.objects.all()
    cars = list(cars.filter(id__in=id))
    print cars
    for s in cars:
        s.nadwozia = Nadwozia.objects.all()
        s.nadwozia = s.nadwozia.filter(Samochod=s.id)
        print s.nadwozia
        for n in s.nadwozia:
            n.silniki = Silniki_Parametry.objects.all()
            n.silniki = n.silniki.filter(Nadwozie=n)
            print n.silniki

    c['cars'] = cars
    c['s_id'] = s_id
    print cars
    return render(request, "porownanie.html", c)

def logout_page(request):
    logout(request)
    return redirect("/")

def moderate(request):
    c={}
    done=False
    succes=''
    if request.method=='POST':
        type=request.POST.get('submit')
        if type == 'dodaj marke':
            marka=addMarka(request.POST)
            if marka.is_valid():
                marka = marka.save(commit=False)
                marka.save()
                succes = "Dodano nowa Marke do bazy"
                done=True
        elif type == 'dodaj samochod':
            samochod=addSamochod(request.POST)
            if samochod.is_valid():
                samochod = samochod.save(commit=False)
                samochod.save()
                succes="Dodano nowy Model do bazy"
                done=True
        elif type == 'dodaj nadwozie':
            nadwozie=addNadwozie(request.POST)
            if nadwozie.is_valid():
                nadwozie = nadwozie.save(commit=False)
                nadwozie.save()
                succes="Dodano nowe Nadwozie do bazy"
                done=True
        elif type == 'dodaj silnik':
            silnik=addSilnik(request.POST)
            if silnik.is_valid():
                silnik = silnik.save(commit=False)
                silnik.save()
                succes="Dodano nowy Silnik do bazy"
                done=True
        elif type == 'dodaj konfiguracje':
            parametry=addParametry(request.POST)
            if parametry.is_valid():
                parametry = parametry.save(commit=False)
                parametry.save()
                succes="Dodano nowa konfiguracje do bazy"
    marka = addMarka()
    samochod = addSamochod()
    nadwozie = addNadwozie()
    silnik = addSilnik()
    parametry = addParametry()
    c['marka'] = marka
    c['samochod'] = samochod
    c['nadwozie'] = nadwozie
    c['silnik'] = silnik
    c['parametry'] = parametry
    c['succes'] = succes
    return render(request, "registration/moderate.html", c)