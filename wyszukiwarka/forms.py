# coding=utf-8
import datetime
from django import forms
from wyszukiwarka.models import *


class SearchForm(forms.ModelForm):
    class Meta:
        model = Wyszukiwanie
        fields = ('Marka', 'Model', 'Rocznik_od', 'Rocznik_do', 'Cena_od', 'Cena_do')
