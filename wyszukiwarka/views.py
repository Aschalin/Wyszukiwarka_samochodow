from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext

from models import *
from django.http import HttpResponse
from wyszukiwarka.forms import *
from base64 import b64encode
from django.core.exceptions import ObjectDoesNotExist

from wyszukiwarka.support import *


def index(request):
    c = {}
    samochody = Samochody.objects.all()
    for s in samochody:
        s.rating = getRating(s.id)

    samochody = sorted(samochody, key=lambda s: -s.rating)[:10]
    nadwozia = Nadwozia.objects.all()
    for n in nadwozia:
        n.rating = getRating(str(n.Samochod.id) + '/' + str(n.id))
    nadwozia = sorted(nadwozia, key=lambda s: -s.rating)[:10]
    silniki = Silniki_Nadwozia.objects.all()
    for s in silniki:
        s.rating = getRating(str(s.Nadwozie.Samochod.id) + '/' + str(s.Nadwozie.id) + '/' + str(s.Silnik.id))
    silniki = sorted(silniki, key=lambda s: -s.rating)[:10]
    komentarze = Komentarze.objects.all().order_by('-Time')[:10]
    for k in komentarze:
        k.Time = k.Time.strftime("%y-%m-%d %H:%M:%S")
        k.Site = getSite(k.site)
    c['komentarze'] = komentarze
    c['samochody'] = samochody
    c['nadwozia'] =nadwozia
    c['silniki'] =silniki
    c['auth'] = len(list(request.user.groups.all()))
    return render(request, "base.html", c)

def wyszukiwanie(request):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            wyszukiwanie = form.save(commit = False)
            wyszukiwanie.save()
            return redirect("/przegladanie/" + str(wyszukiwanie.id))
    else:
        form = SearchForm()
    c['form'] = form
    return render(request, "wyszukiwanie.html", c)

def zaawansowane(request):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    if request.method=='POST':
        form=AdvancedForm(request.POST)
        if form.is_valid():
            zaawansowane = form.save(commit=False)
            zaawansowane.save()
            return redirect("/przegladzaawansowany/" + str(zaawansowane.id))
    else:
        form=AdvancedForm()
    c['form']=form
    c['goto']='zaawansowane'
    return render(request, "zaawansowane.html", c)

def przegladanie(request, s_id = 0):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    baseCars = Samochody.objects.all()
    if s_id != '0':
        try:
            szukane = Wyszukiwanie.objects.get(id = s_id)
            if szukane.Marka:
                marki = Marki.objects.get(Marka = szukane.Marka)
                baseCars = baseCars.filter(Marka = marki.id)
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
        except ObjectDoesNotExist:
            pass
            return redirect("/przegladanie/0/")
    baseCars = baseCars.order_by('Samochod')
    baseCars = baseCars.order_by('Marka')
    page = request.GET.get('page')
    if not page:
        page = 1
    paginator = Paginator(baseCars, 10)
    try:
        cars = paginator.page(page)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    c['cars'] = cars
    c['s_id'] = s_id
    return render(request, "przegladanie.html", c)


def przegladzaawansowany(request, s_id=0):
    c={}
    c['auth'] = len(list(request.user.groups.all()))
    baseSilniki = Silniki_Parametry.objects.all()

    if s_id != '0':
        try:
            szukane = Zaawansowane.objects.get(id=s_id)
            if szukane.Spalanie_od:
                baseSilniki = baseSilniki.filter(Spalanie__gte=szukane.Spalanie_od)
            if szukane.Spalanie_do:
                baseSilniki = baseSilniki.filter(Spalanie__lte=szukane.Spalanie_do)
            if szukane.Przyspieszenie_od_0_do_100_od:
                baseSilniki = baseSilniki.filter(Przyspieszenie__gte=szukane.Przyspieszenie_od_0_do_100_od)
            if szukane.Przyspieszenie_od_0_do_100_do:
                baseSilniki = baseSilniki.filter(Przyspieszenie__lte=szukane.Przyspieszenie_od_0_do_100_do)
            if szukane.Predkosc_maksymalna_od:
                baseSilniki = baseSilniki.filter(VMax__gte=szukane.Predkosc_maksymalna_od)
            if szukane.Predkosc_maksymalna_do:
                baseSilniki = baseSilniki.filter(VMax__lte=szukane.Predkosc_maksymalna_do)
            if szukane.Pojemnosc_silnika_od:
                baseSilniki = baseSilniki.filter(Pojemnosc__gte=szukane.Pojemnosc_silnika_od)
            if szukane.Pojemnosc_silnika_do:
                baseSilniki = baseSilniki.filter(Pojemnosc__lte=szukane.Pojemnosc_silnika_do)
            if szukane.Moc_od:
                baseSilniki = baseSilniki.filter(KM__gte=szukane.Moc_od)
            if szukane.Moc_do:
                baseSilniki = baseSilniki.filter(KM__lte=szukane.Moc_do)
        except ObjectDoesNotExist:
            pass
            return redirect("/przegladzaawansowany/0/")


    baseSilniki = baseSilniki.order_by('Nadwozie')
    page = request.GET.get('page')
    if not page:
       page=1
    paginator = Paginator(baseSilniki, 10)
    try:
        engines = paginator.page(page)
    except EmptyPage:
        engines = paginator.page(paginator.num_pages)
    c['engines']=engines
    c['s_id']=s_id
    return render(request, "przegladzaawansowany.html", c)

def model(request, s_id, c_id):
    c = {}
    car = Samochody.objects.get(id = c_id)
    nadwozia = Nadwozia.objects.all()
    nadwozia = nadwozia.filter(Samochod = car)
    files = Zdjecia.objects.all()
    files = files.filter(Nadwozie__in = nadwozia)
    for f in files:
        f.Plik = b64encode(f.Plik)
    c['car'] = car
    c['s_id'] = s_id
    try:
        c['cenaMax'] = car.Cena + (maxPrice.objects.raw("call samochodMaxPrice(" + c_id + ");"))[0].Cena
    except TypeError:
        pass
    komentarze = handleComments(request)
    rating = handleRating(handlePath(request.path))
    c.update(komentarze)
    c.update(rating)
    c['auth'] = request.user.groups.filter(name = car.Marka).exists()
    c['files'] = files
    c['nadwozia'] = nadwozia
    c['nadwoziaMax'] = list(maxPrice.objects.raw("call nadwozieMaxPrice(" + c_id + ");"))
    print(c['nadwoziaMax'])
    return render(request, "model.html", c)

def nadwozie(request, s_id, c_id, n_id):
    c = {}
    car = Samochody.objects.get(id = c_id)
    nadwozie = Nadwozia.objects.get(id = n_id)
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
    komentarze = handleComments(request)
    rating = handleRating(handlePath(request.path))
    c.update(komentarze)
    c.update(rating)
    c['auth'] = request.user.groups.filter(name = car.Marka).exists()
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
    c = {}
    car = Samochody.objects.get(id = c_id)
    nadwozie = Nadwozia.objects.get(id = n_id)
    silnik = Silniki.objects.get(id = e_id)
    parametry = Silniki_Nadwozia.objects.all()
    parametry = parametry.filter(Nadwozie = nadwozie)
    parametry = parametry.filter(Silnik = silnik)
    komentarze = handleComments(request)
    rating = handleRating(handlePath(request.path))
    c.update(komentarze)
    c.update(rating)
    c['auth'] = request.user.groups.filter(name = car.Marka).exists()
    c['car'] = car
    c['s_id'] = s_id
    c['nadwozie'] = nadwozie
    c['silnik'] = silnik
    c['parametry'] = parametry[0]
    return render(request, "silnik.html", c)

def porownanie(request, s_id):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    id = request.GET.getlist('cars')
    cars = Samochody.objects.all()
    cars = list(cars.filter(id__in = id))
    print cars
    for s in cars:
        s.nadwozia = Nadwozia.objects.all()
        s.nadwozia = s.nadwozia.filter(Samochod = s.id)
        print s.nadwozia
        for n in s.nadwozia:
            n.silniki = Silniki_Parametry.objects.all()
            n.silniki = n.silniki.filter(Nadwozie = n)
            print n.silniki

    c['cars'] = cars
    c['s_id'] = s_id
    print cars
    return render(request, "porownanie.html", c)

def logout_page(request):
    logout(request)
    return redirect("/")

def moderate(request):
    c = {}
    done = False
    succes = ''
    auth = list(request.user.groups.all())
    if request.method == 'POST':
        type = request.POST.get('submit')
        if type == 'dodaj marke':
            marka = markaForm(request.POST)
            if marka.is_valid():
                if 'admin' in auth['Group']:
                    marka = marka.save(commit = False)
                    marka.save()
                    succes = "Dodano nowa Marke do bazy"
                    done = True
                else:
                    succes = "nie masz wystarczajacych uprawnien"
        elif type == 'dodaj samochod':
            samochod = samochodForm(request.POST)
            if samochod.is_valid():
                samochod = samochod.save(commit = False)
                if request.user.groups.filter(name = samochod.Marka).exists():
                    samochod.save()
                    succes = "Dodano nowy Model do bazy"
                    done = True
                else:
                    succes = "nie masz wystarczajacych uprawnien"
        elif type == 'dodaj nadwozie':
            nadwozie = nadwozieForm(request.POST)
            if nadwozie.is_valid():
                nadwozie = nadwozie.save(commit = False)
                nadwozie.save()
                succes = "Dodano nowe Nadwozie do bazy"
                done = True
        elif type == 'dodaj silnik':
            silnik = silnikForm(request.POST)
            if silnik.is_valid():
                silnik = silnik.save(commit = False)
                silnik.save()
                succes = "Dodano nowy Silnik do bazy"
                done = True
        elif type == 'dodaj konfiguracje':
            parametry = parametryForm(request.POST)
            if parametry.is_valid():
                parametry = parametry.save(commit = False)
                parametry.save()
                succes = "Dodano nowa konfiguracje do bazy"
    c['marka'] = markaForm()
    c['samochod'] = samochodForm()
    c['nadwozie'] = nadwozieForm()
    c['silnik'] = silnikForm()
    c['parametry'] = parametryForm()
    c['succes'] = succes
    c['auth'] = len(auth)
    return render(request, "registration/moderate.html", c)

def editSamochod(request, s_id, c_id):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    samochod = Samochody.objects.get(id = c_id)
    if request.method == 'POST':
        form = samochodForm(request.POST, instance = samochod)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            ret = str("/szczegoly/" + s_id + "/" + c_id)
            return redirect("/szczegoly/" + s_id + "/" + c_id)
    else:
        c['form'] = samochodForm(instance = samochod)
    c['type'] = "samochodu"
    return render(request, "registration/editDB.html", c)

def editNadwozie(request, s_id, c_id, n_id):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    nadwozie = Nadwozia.objects.get(id = n_id)
    if request.method == 'POST':
        form = nadwozieForm(request.POST, instance = nadwozie)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            return redirect("/szczegoly/" + s_id + "/" + c_id + "/" + n_id)
    else:
        c['form'] = nadwozieForm(instance = nadwozie)
    c['type'] = "nadwozia"
    return render(request, "registration/editDB.html", c)

def editSilnik(request, s_id, c_id, n_id, e_id):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    silnik = Silniki.objects.get(id = e_id)
    if request.method == 'POST':
        form = silnikForm(request.POST, instance = silnik)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            return redirect("/szczegoly/" + s_id + "/" + c_id + "/" + n_id + "/" + e_id)
    else:
        c['form'] = silnikForm(instance = silnik)
    c['type'] = "silnika"
    return render(request, "registration/editDB.html", c)

def editParametry(request, s_id, c_id, n_id, e_id):
    c = {}
    c['auth'] = len(list(request.user.groups.all()))
    nadwozie = Nadwozia.objects.get(id = n_id)
    silnik = Silniki.objects.get(id = e_id)
    parametry = Silniki_Nadwozia.objects.all()
    parametry = parametry.filter(Nadwozie = nadwozie)
    parametry = parametry.filter(Silnik = silnik)
    if request.method == 'POST':
        form = parametryForm(request.POST, instance = parametry[0])
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            return redirect("/szczegoly/" + s_id + "/" + c_id + "/" + n_id + "/" + e_id)
    else:
        c['form'] = parametryForm(instance = parametry[0])
    c['type'] = "silnika"
    return render(request, "registration/editDB.html", c)

def szczegolysilnika(request, s_id, p_id):
    parametry = Silniki_Nadwozia.objects.get(id=p_id)
    c_id = str(parametry.Nadwozie.Samochod.id)
    n_id = str(parametry.Nadwozie.id)
    e_id = str(parametry.Silnik.id)
    return redirect("/szczegoly/" + s_id + "/" + c_id + "/" + n_id + "/" + e_id)

def register(request):
    c={}
    c['auth'] = len(list(request.user.groups.all()))
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        form = registerForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print form.errors
    else:
        form = registerForm()
    c['form'] = form
    c['registered'] = registered
    return render(request, 'registration/register.html', c)