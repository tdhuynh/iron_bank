# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iron_bank_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
