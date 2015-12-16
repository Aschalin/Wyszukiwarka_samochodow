from django.db import models

# Create your models here.


class Samochody(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(default='', max_length=30)
    Model = models.CharField(default='', max_length=30)
    Rocznik = models.IntegerField(default=2015)
    Cena = models.IntegerField(default='')

class Wyszukiwanie(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Marka = models.CharField(default='', max_length=30)
    Model = models.CharField(default='', max_length=30)
    Rocznik_od = models.IntegerField(default=2015)
    Rocznik_do = models.IntegerField()
    Cena_od = models.IntegerField(default='')
    Cena_do = models.IntegerField(default='')

    def __unicode__(self):
        return self.Model