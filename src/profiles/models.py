from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django_countries.fields import CountryField
from .utils import sme_choices
import datetime

User = settings.AUTH_USER_MODEL

class SMEProfile(models.Model):
    # Retrieve all choices
    LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR = sme_choices()
    # Assign model fields
    user = models.ForeignKey(User)
    description = models.CharField(max_length=1500, blank=True, null=True)
    legal_struct = models.CharField(max_length=2, choices=LEGAL_STRUCT)
    ownership = models.CharField(max_length=2, choices=OWNERSHIP)
    country = CountryField(blank_label='(select country)')
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    currency = models.CharField(max_length=50, choices=CURRENCIES)
    lkin_urls = models.URLField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=50, choices=SECTOR)
    avatar = models.ImageField(default="static/logos/logo.png")

    def __str__(self):
        return self.user.__str__()
