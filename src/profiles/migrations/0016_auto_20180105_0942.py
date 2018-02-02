# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-05 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20180105_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorprofile',
            name='deal',
            field=models.CharField(choices=[('e', 'Equity'), ('t', 'Trade'), ('d', 'Debt')], max_length=1),
        ),
    ]