from django.db import models

# Create your models here.


class Samochody(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    Marka = models.TextField(default='', max_length=255)
    Model = models.TextField(default='', max_length=255)
    Rocznik = models.IntegerField(default=2015, max_length=4)
    Cena = models.IntegerField(default='', max_length=8)

    def __unicode__(self):
        return self.Model