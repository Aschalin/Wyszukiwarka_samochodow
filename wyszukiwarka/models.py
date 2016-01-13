from django.db import models


# Create your models here.

class Marki(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(default='', max_length=30)
    Kraj = models.CharField(default='', max_length=30)
    WWW = models.URLField()

    def __unicode__(self):
        return self.Marka

    class Meta:
        managed = False


class Samochody(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.ForeignKey(Marki, db_column='idMarka')
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Cena = models.IntegerField(default='')

    def __unicode__(self):
        return self.Model

    class Meta:
        managed = False


class Nadwozia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Samochod = models.ForeignKey(Samochody, db_column='idSamochod')
    Rodzaj = models.CharField(default='', max_length=30)
    Oplata = models.IntegerField(default='0')

    def __unicode__(self):
        return self.Rodzaj

    class Meta:
        managed = False


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
    Paliwo = models.CharField(choices=PaliwoChoices, default=Benzyna, max_length=1)
    Pojemnosc = models.FloatField(default=1.0)
    KM = models.IntegerField(default='100')

    def __unicode__(self):
        return self.Rodzaj

    class Meta:
        managed = False


class Silniki_Nadwozia(models.Model):
    Nadwozie = models.ForeignKey(Nadwozia, db_column='idNadwozie')
    Silnik = models.ForeignKey(Silniki, db_column='idSilnik', related_name='parametry')
    Spalanie = models.FloatField(default='')
    Przyspieszenie = models.FloatField(default='')
    VMax = models.IntegerField(default='0')
    Oplata = models.IntegerField(default='0')

    def __unicode__(self):
        return str(self.Silnik) or u''

    class Meta:
        managed = False


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

    class Meta:
        managed = False


class Zdjecia(models.Model):
    Plik = models.BinaryField(editable=False)
    Nadwozie = models.ForeignKey(Nadwozia, db_column='idNadwozie')

    def __unicode__(self):
        return self.Nadwozie

    class Meta:
        managed = False


class Porownania(models.Model):
    Benzyna = 'B'
    Diesel = 'D'
    Gaz = 'G'
    PaliwoChoices = (
        (Benzyna, 'Benzyna'),
        (Diesel, 'Diesel'),
        (Gaz, 'Gaz'),
    )
    id = models.CharField(primary_key=True, max_length=35, editable=False)
    Marka = models.ForeignKey(Marki, db_column='idMarka')
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Nadwozie = models.CharField(default='', max_length=30)
    Silnik = models.CharField(default='', max_length=45)
    Paliwo = models.CharField(choices=PaliwoChoices, default=Benzyna, max_length=1)
    Spalanie = models.FloatField(default='')
    Przyspieszenie = models.FloatField(default='')
    VMax = models.IntegerField(default='0')
    Cena = models.BigIntegerField(default='')

    class Meta:
        managed = False

class maxPrice(models.Model):
    id = models.CharField(primary_key=True, max_length=35, editable=False)
    Cena = models.BigIntegerField(default='')
