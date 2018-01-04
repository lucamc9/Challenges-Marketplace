from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django_countries.fields import CountryField
from .utils import sme_choices
import datetime
from django.core.urlresolvers import reverse

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
    avatar = models.ImageField(default="static/logos/logo-white.png")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_description(self):
        return self.description

    def get_legal_struct(self):
        return self.legal_struct

    def get_ownership(self):
        return self.ownership

    def get_country(self):
        return self.country

    def get_year(self):
        return self.year

    def get_currency(self):
        return self.currency

    def get_lkin_urls(self):
        return self.lkin_urls

    def get_sector(self):
        return self.sector

    def get_avatar(self):
        return self.avatar

class InvestorProfile(models.Model):
    LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR = sme_choices()
    DEAL_TYPE = (
        ('Equity', 'Equity'),
        ('Trade', 'Trade'),
        ('Debt', 'Debt')
    )
    user = models.ForeignKey(User)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    deal = models.CharField(max_length=1, choices=DEAL_TYPE)
    sector = models.CharField(max_length=50, choices=SECTOR)
    avatar = models.ImageField(default="static/logos/logo-white.png")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_full_name(self):
        return self.full_name

    def get_description(self):
        return self.description

    def get_deal(self):
        return self.deal

    def get_sector(self):
        return self.sector

    def get_avatar(self):
        return self.avatar



