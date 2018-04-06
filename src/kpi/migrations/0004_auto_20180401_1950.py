# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-01 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0003_auto_20180401_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdata',
            name='cash_flow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='graphdata',
            name='expenditures',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='graphdata',
            name='flow_month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='January', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphdata',
            name='revenues',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]