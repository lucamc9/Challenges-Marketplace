from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django_countries.fields import CountryField
from .utils import sme_choices
import datetime
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class SMEProfile(models.Model):
    # Retrieve all choices
    LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR = sme_choices()
    # Assign model fields
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    legal_struct = models.CharField(max_length=2, choices=LEGAL_STRUCT)
    ownership = models.CharField(max_length=2, choices=OWNERSHIP)
    country = CountryField(blank_label='(select country)')
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    currency = models.CharField(max_length=50, choices=CURRENCIES)
    lkin_urls = models.URLField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=50, choices=SECTOR)
    avatar = models.ImageField(upload_to='pictures/', default='pictures/logo-white.png')
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('profiles:detail-sme', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

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
        ('e', 'Equity'),
        ('t', 'Trade'),
        ('d', 'Debt')
    )
    user = models.ForeignKey(User)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    deal = models.CharField(max_length=1, choices=DEAL_TYPE)
    sector = models.CharField(max_length=50, choices=SECTOR)
    avatar = models.ImageField(default="static/logos/logo-white.png")
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

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

class StaffProfile(models.Model):
    user = models.ForeignKey(User)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(default="static/logos/logo-white.png")
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('profiles:detail-staff', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_full_name(self):
        return self.full_name

    def get_role(self):
        return self.role

    def get_avatar(self):
        return self.avatar


def pre_save_receiver(sender, instance, *args, **kwargs):
    # Make a slug out of the user's email for the specific profile
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=SMEProfile)
pre_save.connect(pre_save_receiver, sender=StaffProfile)
pre_save.connect(pre_save_receiver, sender=InvestorProfile)


