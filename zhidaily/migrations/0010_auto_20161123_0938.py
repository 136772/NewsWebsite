# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhidaily', '0009_auto_20161123_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(upload_to='AD/%Y%m%d'),
        ),
    ]
