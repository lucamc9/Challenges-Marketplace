# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-18 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171218_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
