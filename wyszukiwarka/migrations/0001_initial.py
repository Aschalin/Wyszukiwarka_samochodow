# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marki',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('Marka', models.CharField(default=b'', max_length=30)),
                ('Kraj', models.CharField(default=b'', max_length=30)),
                ('WWW', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Nadwozia',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('Rodzaj', models.CharField(default=b'', max_length=30)),
                ('Oplata', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='Samochody',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('Model', models.CharField(default=b'', max_length=30)),
                ('Rocznik', models.IntegerField(default=2015)),
                ('Cena', models.IntegerField(default=b'')),
                ('Marka', models.ForeignKey(to='wyszukiwarka.Marki', db_column=b'idMarka')),
            ],
        ),
        migrations.CreateModel(
            name='Silnik_Nadwozie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Zuzycie_Paliwa', models.FloatField(default=b'')),
                ('Przyspieszenie', models.FloatField(default=b'', db_column=b'0-100 km/h')),
                ('VMax', models.IntegerField(default=b'0')),
                ('Oplata', models.IntegerField(default=b'0')),
                ('Nadwozie', models.ForeignKey(to='wyszukiwarka.Nadwozia', db_column=b'idNadwozie')),
            ],
        ),
        migrations.CreateModel(
            name='Silniki',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('Rodzaj', models.CharField(default=b'', max_length=10)),
                ('Paliwo', models.CharField(default=b'B', max_length=1, choices=[(b'B', b'Benzyna'), (b'D', b'Diesel'), (b'G', b'Gaz')])),
                ('Pojemnosc', models.FloatField(default=1.0)),
                ('KM', models.IntegerField(default=b'100')),
            ],
        ),
        migrations.CreateModel(
            name='Wyszukiwanie',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('Marka', models.CharField(max_length=30, null=True, blank=True)),
                ('Model', models.CharField(max_length=30, null=True, blank=True)),
                ('Rocznik_od', models.IntegerField(null=True, blank=True)),
                ('Rocznik_do', models.IntegerField(default=2015, null=True, blank=True)),
                ('Cena_od', models.IntegerField(default=b'', null=True, blank=True)),
                ('Cena_do', models.IntegerField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='silnik_nadwozie',
            name='Silnik',
            field=models.ForeignKey(related_name='parametry', db_column=b'idSilnik', to='wyszukiwarka.Silniki'),
        ),
        migrations.AddField(
            model_name='nadwozia',
            name='Samochod',
            field=models.ForeignKey(to='wyszukiwarka.Samochody', db_column=b'idSamochod'),
        ),
    ]
