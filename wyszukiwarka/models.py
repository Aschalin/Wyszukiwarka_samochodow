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
        verbose_name_plural = 'Marki'


class Samochody(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.ForeignKey(Marki, db_column='idMarka')
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Cena = models.IntegerField(default='')

    def __unicode__(self):
        return str(self.Marka) + ' ' + self.Model

    class Meta:
        managed = False
        verbose_name_plural = 'Modele'


class Nadwozia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Samochod = models.ForeignKey(Samochody, db_column='idSamochod')
    Rodzaj = models.CharField(default='', max_length=30)
    Oplata = models.IntegerField(default='0')

    def __unicode__(self):
        return str(self.Samochod) + ' ' + self.Rodzaj

    class Meta:
        managed = False
        verbose_name_plural = 'Nadwozia'


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
        return str(self.Pojemnosc) + ' ' + self.Rodzaj + ' ' + str(self.KM) + 'KM'

    class Meta:
        managed = False
        verbose_name_plural = 'Silniki'


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
        verbose_name_plural = 'Konfiguracje'


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

class Zaawansowane(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Spalanie_od = models.FloatField(default='', blank=True, null=True)
    Spalanie_do = models.FloatField(default='', blank=True, null=True)
    Przyspieszenie_od_0_do_100_od = models.FloatField(default='', blank=True, null=True)
    Przyspieszenie_od_0_do_100_do = models.FloatField(default='', blank=True, null=True)
    Predkosc_maksymalna_od = models.IntegerField(default='', blank=True, null=True)
    Predkosc_maksymalna_do = models.IntegerField(default='', blank=True, null=True)
    Pojemnosc_silnika_od = models.FloatField(default='', blank=True, null=True)
    Pojemnosc_silnika_do = models.FloatField(default='', blank=True, null=True)
    Moc_od = models.IntegerField(default='', blank=True, null=True)
    Moc_do = models.IntegerField(default='', blank=True, null=True)

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
        verbose_name_plural = 'Zdjecia'


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


class Silniki_Parametry(models.Model):
    Benzyna = 'B'
    Diesel = 'D'
    Gaz = 'G'
    PaliwoChoices = (
        (Benzyna, 'Benzyna'),
        (Diesel, 'Diesel'),
        (Gaz, 'Gaz'),
    )
    id = models.IntegerField(primary_key=True, editable=False)
    Silnik = models.CharField(default='', max_length=45)
    Paliwo = models.CharField(choices=PaliwoChoices, default=Benzyna, max_length=1)
    Spalanie = models.FloatField(default='')
    Przyspieszenie = models.FloatField(default='')
    VMax = models.IntegerField(default='0')
    Cena = models.BigIntegerField(default='')
    Nadwozie = models.ForeignKey(Nadwozia, db_column='idNadwozie')

    class Meta:
        managed = False
        verbose_name_plural = 'Parametry silnikow'


class maxPrice(models.Model):
    id = models.CharField(primary_key=True, max_length=35, editable=False)
    Cena = models.BigIntegerField(default='')

    class Meta:
        managed = False
