# coding=utf-8
import datetime
from django import forms
from wyszukiwarka.models import *


class SearchForm(forms.Form):
    Marka = forms.CharField(help_text=u"Marka", required=False)
    Model = forms.CharField(help_text=u"Model", required=False)
    rocznik_od = forms.IntegerField(help_text=u"Rocznik od", initial=0, required=False)
    rocznik_do = forms.IntegerField(help_text=u"do", initial=2015, required=False)
    cena_od = forms.IntegerField(help_text=u"cena od", required=False)
    cena_do = forms.IntegerField(help_text=u"cena do", required=False)

class HiddenSearchForm(forms.Form):
    Marka = forms.CharField(widget=forms.HiddenInput(), required=False)
    Model = forms.CharField(widget=forms.HiddenInput(), required=False)
    rocznik_od = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    rocznik_do = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    cena_od = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    cena_do = forms.IntegerField(widget=forms.HiddenInput(), required=False)