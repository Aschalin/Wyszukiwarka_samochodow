# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyszukiwarka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Silnik_Nadwozie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Zuzycie_Paliwa', models.FloatField(default=b'')),
                ('Przyspieszenie', models.FloatField(default=b'', db_column=b'0-100 km/h')),
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
                ('KM', models.FloatField(default=b'100')),
            ],
        ),
        migrations.AddField(
            model_name='silnik_nadwozie',
            name='Silnik',
            field=models.ForeignKey(to='wyszukiwarka.Silniki', db_column=b'idSilnik'),
        ),
    ]
