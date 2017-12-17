from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.ForeignKey(User)
