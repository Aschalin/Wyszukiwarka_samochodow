from django.test import TestCase
from views import *
from models import *

# Create your tests here.
class ViewsTestCase(TestCase):
    def setUp(self):
        self.marki = []
        self.samochody = []
        self.nadwozia = []
        self.silniki = []
        self.parametry = []

        for e in range (1, 3):
            self.silniki = Silniki.objects.create(
                Rodzaj = 'test',
                Paliwo = 'Benzyna',
                Pojemnosc = e,
                KM = 100 + 30 * e
            )

        for m in range(1, 2):
            marka=Marki.objects.create(
                Marka = 'm' + m,
                Kraj = 'k' + m,
                WWW = 'http//:www.m' + m + '.pl'
            )
            self.marki.append(marka)
            for c in range(1, 3):
                samochod = Samochody.objects.create(
                    Marka = marka,
                    Model = 'c' + c,
                    Rocznik = 2015,
                    Cena = 50000 * c + 10000 * m
                )
                self.samochody.append(samochod),
                for n in range(0, 2):
                    nadwozie = Nadwozia.objects.create(
                        Samochod = samochod,
                        Rodzaj = 'n' + n,
                        Oplata = 500 * n
                    )
                    self.nadwozia=nadwozie
                    for e in range(0, 2):
                        parametr = Silniki_Nadwozia.objects.create(
                            Nadwozie = nadwozie,
                            Silnik = self.silniki[e],
                            Spalanie = 3 * e + n,
                            Przyspieszenie = 5+n - e,
                            Vmax = 200 - 5 * n + 10 * e,
                            Oplata = e * (500 + 100 * n),
                        )



    def tearDown(self):
        del self.marki
        del self.samochody
        del self.nadwozia
        del self.silniki
        del self.parametry

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

