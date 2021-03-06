# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-22 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0004_auto_20180220_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostics',
            old_name='IT',
            new_name='environmental',
        ),
        migrations.RenameField(
            model_name='diagnostics',
            old_name='environ',
            new_name='operations',
        ),
        migrations.RenameField(
            model_name='diagnostics',
            old_name='facilities',
            new_name='sales',
        ),
        migrations.RemoveField(
            model_name='diagnostics',
            name='hr',
        ),
        migrations.RemoveField(
            model_name='diagnostics',
            name='legal',
        ),
        migrations.RemoveField(
            model_name='diagnostics',
            name='manproc',
        ),
        migrations.RemoveField(
            model_name='diagnostics',
            name='marketing',
        ),
        migrations.RemoveField(
            model_name='diagnostics',
            name='staff',
        ),
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
