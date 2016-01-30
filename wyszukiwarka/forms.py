# coding=utf-8
import datetime
from django import forms
from django.contrib.auth.models import User

from wyszukiwarka.models import *
from django.core.exceptions import ObjectDoesNotExist

class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class SearchForm(forms.ModelForm):
    class Meta:
        model = Wyszukiwanie
        fields = ('Marka', 'Model', 'Rocznik_od', 'Rocznik_do', 'Cena_od', 'Cena_do')

class AdvancedForm(forms.ModelForm):
    class Meta:
        model = Zaawansowane
        fields = ('Spalanie_od','Spalanie_do', 'Przyspieszenie_od_0_do_100_od', 'Przyspieszenie_od_0_do_100_do', 'Predkosc_maksymalna_od', 'Predkosc_maksymalna_do', 'Pojemnosc_silnika_od', 'Pojemnosc_silnika_do', 'Moc_od', 'Moc_do')

class markaForm(forms.ModelForm):
    class Meta:
        model = Marki
        fields = ('Marka', 'Kraj', 'WWW')


class samochodForm(forms.ModelForm):
    class Meta:
        model = Samochody
        fields = ('Marka', 'Model', 'Rocznik', 'Cena')


class nadwozieForm(forms.ModelForm):
    class Meta:
        model = Nadwozia
        fields = ('Samochod', 'Rodzaj', 'Oplata')


class silnikForm(forms.ModelForm):
    class Meta:
        model = Silniki
        fields = ('Rodzaj', 'Paliwo', 'Pojemnosc', 'KM')


class parametryForm(forms.ModelForm):
    class Meta:
        model = Silniki_Nadwozia
        fields = ('Nadwozie', 'Silnik', 'Spalanie', 'Przyspieszenie', 'VMax', 'Oplata')

class komentarzForm(forms.ModelForm):
    class Meta:
        model = Komentarze
        fields = ('Text',)
