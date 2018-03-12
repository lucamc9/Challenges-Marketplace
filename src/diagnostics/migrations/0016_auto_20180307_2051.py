# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0015_auto_20180307_2047'),
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
