# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-25 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_smeprofile_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smeprofile',
            name='sector',
            field=models.CharField(choices=[('Agriculture', (('fruit', 'Fruit'), ('coffee', 'Coffee'), ('nuts', 'Nuts'), ('tea', 'Tea'), ('cocoa', 'Cocoa'), ('sugar', 'Sugar'), ('forest', 'Forest'), ('bamboo', 'Bamboo'), ('vegetables', 'Vegetables'), ('meat', 'Meat'), ('fish', 'Fish'), ('shea', 'Shea'), ('moringa', 'Moringa'))), ('Energy & Water', (('stoves', 'Stoves'), ('solar', 'Solar'), ('lamps', 'Lamp/Kits'), ('bio', 'Bio/Gar'), ('wind', 'Wind/Hydro'), ('mini-grid', 'Mini-Grid'), ('water-filt', 'Water filtration'), ('briquettes', 'Briquettes/Pellets'))), ('Waste Management', (('recycling', 'Recycling'), ('sewerage', 'Sewerage'), ('collection', 'Collection'))), ('Health & Social', (('health', 'Health Foods/Products'), ('excercise', 'Excercise Items'), ('medical', 'Medical Facilities/Treatment'), ('care', 'Care Provision'))), ('Tourism', (('conservation', 'Conservation'), ('community', 'Community Engagement'))), ('Craft', (('leather', 'Leather/Textiles/Plant Fibres'), ('wood', 'Wood'), ('cosmetics', 'Cosmetics'), ('accessories', 'Accessories'), ('household', 'Household Items'), ('jewellery', 'Jewellery'), ('coffins', 'Coffins'), ('fashion', 'Fashion'))), ('Finance', (('provision', 'Finance Provision to Individuals'), ('micro-leasing', 'Micro-leasing'))), ('Education', (('low', 'Low Fee Private Schooling'), ('training', 'Vocational Training'))), ('Construction & Manufacturing', (('building', 'House Building'), ('roads', 'Roads'), ('manufacturing', 'Technical Manufacturing'))), ('Accomodation & Food Services', (('hotels', 'Hotels'), ('restaurants', 'Restaurants'), ('catering', 'Catering'), ('bakery', 'Bakery'), ('delivery', 'Food Delivery'))), ('Professional & Support Services', (('law', 'Law'), ('pr', 'PR'), ('real', 'Real Estate'))), ('Other', (('entertainment', 'Entertainment & Arts'), ('tech', 'Technology')))], max_length=50),
        ),
    ]
