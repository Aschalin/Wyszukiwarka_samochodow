# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wyszukiwarka',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('Marka', models.TextField(default=b'')),
                ('Model', models.TextField(default=b'')),
                ('Rocznik', models.IntegerField(default=2015)),
                ('Cena', models.IntegerField(default=b'')),
            ],
        ),
    ]
