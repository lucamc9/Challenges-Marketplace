# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-03 17:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=1500, null=True)),
                ('qualifications', models.CharField(blank=True, max_length=1500, null=True)),
                ('exit', models.CharField(blank=True, max_length=1500, null=True)),
                ('summary', models.CharField(blank=True, max_length=1500, null=True)),
                ('competitors', models.CharField(blank=True, max_length=1500, null=True)),
                ('customers', models.CharField(blank=True, max_length=1500, null=True)),
                ('market', models.CharField(blank=True, max_length=1500, null=True)),
                ('problem', models.CharField(blank=True, max_length=1500, null=True)),
                ('solution', models.CharField(blank=True, max_length=1500, null=True)),
                ('strategy', models.CharField(blank=True, max_length=1500, null=True)),
                ('advantages', models.CharField(blank=True, max_length=1500, null=True)),
                ('financials', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
