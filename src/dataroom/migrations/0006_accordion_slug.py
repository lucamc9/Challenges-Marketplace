# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-14 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataroom', '0005_auto_20180314_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordion',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
