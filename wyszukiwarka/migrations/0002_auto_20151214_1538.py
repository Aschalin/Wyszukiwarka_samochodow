# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyszukiwarka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Samochody',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('Marka', models.TextField(default=b'', max_length=255)),
                ('Model', models.TextField(default=b'', max_length=255)),
                ('Rocznik', models.IntegerField(default=2015, max_length=4)),
                ('Cena', models.IntegerField(default=b'', max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Wyszukiwarka',
        ),
    ]
