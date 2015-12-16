from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from django.http import HttpResponse

from models import *
from django.http import HttpResponse

# Create your views here.
from wyszukiwarka.forms import *


def index(request):
    return render(request, "base.html", {})

def wyszukiwanie(request):
    c={}
    form=SearchForm(request.POST)
    c['form']=form
    return render(request, "wyszukiwanie.html", c)


def przegladanie(request):
    c={}
    baseCars = Samochody.objects.all()
    page = request.POST.get('page')
    form=HiddenSearchForm(request.POST)
    if request.method=='POST':
        marka = request.POST.get('Marka')
        model = request.POST.get('Model')
        cena_od = request.POST.get('cena_od')
        if marka:
            baseCars = baseCars.filter(Marka = marka)
        if model:
            baseCars = baseCars.filter(Model = model)
        if cena_od:
            baseCars = baseCars.filter(Cena__gte = cena_od)
    baseCars = baseCars.order_by('Marka')
    page = request.POST.get('page')
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
    c['form']=form
    c['page']=page
    return render(request, "przegladanie.html", c)

def szczegoly(request):
    c={}
    id=request.GET.get('id')
    car = Samochody.objects.get(id=id)
    c['car'] = car
    return render(request, "szczegoly.html", c)