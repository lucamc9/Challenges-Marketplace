# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-05 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplan', '0003_auto_20180203_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessplan',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
