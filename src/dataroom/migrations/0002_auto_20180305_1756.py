# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-05 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='file',
            field=models.FileField(upload_to='competition/'),
        ),
    ]
