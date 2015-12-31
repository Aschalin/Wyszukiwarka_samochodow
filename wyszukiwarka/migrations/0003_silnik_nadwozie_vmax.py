# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyszukiwarka', '0002_auto_20151228_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='silnik_nadwozie',
            name='VMax',
            field=models.IntegerField(default=b'0'),
        ),
    ]
