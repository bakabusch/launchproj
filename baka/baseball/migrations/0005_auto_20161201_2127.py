# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_auto_20161201_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statline',
            name='wraa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
