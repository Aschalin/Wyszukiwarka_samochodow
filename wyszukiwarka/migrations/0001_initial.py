# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('Marka', models.CharField(default=b'', max_length=30)),
                ('Model', models.CharField(default=b'', max_length=30)),
                ('Rocznik', models.IntegerField(default=2015)),
                ('Cena', models.IntegerField(default=b'')),
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
            model_name='nadwozia',
            name='Samochod',
            field=models.ForeignKey(to='wyszukiwarka.Samochody', db_column=b'idSamochod'),
        ),
    ]
