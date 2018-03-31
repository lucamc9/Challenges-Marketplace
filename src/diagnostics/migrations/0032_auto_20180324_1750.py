# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-24 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0031_auto_20180324_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Management_10',
            field=models.IntegerField(choices=[(1, 'No'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Processes_0',
            field=models.IntegerField(choices=[(1, 'No'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Processes_1',
            field=models.IntegerField(choices=[(1, 'No - not applicable'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
    ]
