# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhidaily', '0007_advert'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]
