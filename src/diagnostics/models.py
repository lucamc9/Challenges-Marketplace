from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django_countries.fields import CountryField
import datetime
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL


