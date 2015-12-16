from django.db import models

# Create your models here.


class Samochody(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(default='', max_length=30)
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Cena = models.IntegerField(default='')

    def __unicode__(self):
        return self.Model


class Nadwozia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Samochod=models.ForeignKey(Samochody, db_column='idSamochod')
    Rodzaj=models.CharField(default='', max_length=30)
    Oplata=models.IntegerField(default='0')

    def __unicode__(self):
        return self.Model


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