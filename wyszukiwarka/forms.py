# coding=utf-8
import datetime
from django import forms
from wyszukiwarka.models import *
from django.core.exceptions import ObjectDoesNotExist

class SearchForm(forms.ModelForm):
    class Meta:
        model = Wyszukiwanie
        fields = ('Marka', 'Model', 'Rocznik_od', 'Rocznik_do', 'Cena_od', 'Cena_do')

class addMarka(forms.ModelForm):
    class Meta:
        model = Marki
        fields = ('Marka', 'Kraj', 'WWW')

class addSamochod(forms.ModelForm):
    class Meta:
        model = Samochody
        fields = ('Marka', 'Model', 'Rocznik', 'Cena')

class addNadwozie(forms.ModelForm):
    class Meta:
        model = Nadwozia
        fields = ('Samochod', 'Rodzaj', 'Oplata')

class addSilnik(forms.ModelForm):
    class Meta:
        model = Silniki
        fields = ('Rodzaj', 'Paliwo', 'Pojemnosc', 'KM')

class addParametry(forms.ModelForm):
    class Meta:
        model = Silniki_Nadwozia
        fields = ('Nadwozie', 'Silnik', 'Spalanie', 'Przyspieszenie', 'VMax', 'Oplata')