# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-24 18:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMEProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('legal_struct', models.CharField(choices=[('BC', 'Benefit Corporation'), ('CO', 'Co-op'), ('CR', 'Corporation'), ('LL', 'Limited Liability Company'), ('NP', 'Non-Profit/Non-Governmental Organization'), ('PT', 'Partnership'), ('SP', 'Sole-Proprietorship'), ('OT', 'Other')], max_length=2)),
                ('ownership', models.CharField(choices=[('WO', 'Woman Owned'), ('YO', 'Youth Owned'), ('LO', 'Local Owned'), ('IO', 'International Owned'), ('OT', 'Other')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
