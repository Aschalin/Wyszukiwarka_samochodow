from django.db import models


# Create your models here.

class Marki(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(default='', max_length=30)
    Kraj = models.CharField(default='', max_length=30)
    WWW = models.URLField()

    def __unicode__(self):
        return self.Marka

class Samochody(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.ForeignKey(Marki,db_column='idMarka')
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Cena = models.IntegerField(default='')

    def __unicode__(self):
        return self.Model


class Nadwozia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Samochod = models.ForeignKey(Samochody, db_column='idSamochod')
    Rodzaj = models.CharField(default='', max_length=30)
    Oplata = models.IntegerField(default='0')

    def __unicode__(self):
        return self.Rodzaj


class Silniki(models.Model):
    Benzyna = 'B'
    Diesel = 'D'
    Gaz = 'G'
    PaliwoChoices = (
        (Benzyna, 'Benzyna'),
        (Diesel, 'Diesel'),
        (Gaz, 'Gaz'),
    )
    id = models.AutoField(primary_key=True, editable=False)
    Rodzaj = models.CharField(default='', max_length=10)
    Paliwo = models.CharField(choices=PaliwoChoices,default=Benzyna, max_length=1)
    Pojemnosc = models.FloatField(default=1.0)
    KM = models.IntegerField(default='100')


    def __unicode__(self):
        return self.Rodzaj


class Silniki_Nadwozia(models.Model):
    Nadwozie = models.ForeignKey(Nadwozia, db_column='idNadwozie')
    Silnik = models.ForeignKey(Silniki, db_column='idSilnik', related_name = 'parametry')
    Zuzycie_Paliwa = models.FloatField(default='')
    Przyspieszenie = models.FloatField(default='', db_column='0-100 km/h')
    VMax = models.IntegerField(default='0')
    Oplata = models.IntegerField(default='0')

    def __unicode__(self):
        return str(self.Silnik) or u''


class Wyszukiwanie(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(max_length=30, blank=True, null=True)
    Model = models.CharField(max_length=30, blank=True, null=True)
    Rocznik_od = models.IntegerField(blank=True, null=True)
    Rocznik_do = models.IntegerField(default=2015, blank=True, null=True)
    Cena_od = models.IntegerField(default='', blank=True, null=True)
    Cena_do = models.IntegerField(default='', blank=True, null=True)

    def __unicode__(self):
        return self.Model

class Zdjecia(models.Model):
    Plik = models.BinaryField(editable=False)
    Nadwozie = models.ForeignKey(Nadwozia, db_column='idNadwozie')

    def __unicode__(self):
        return self.Nadwozie
