# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-03 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20180105_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smeprofile',
            name='avatar',
            field=models.ImageField(default='pictures/logo-white.png', upload_to='pictures/'),
        ),
    ]
