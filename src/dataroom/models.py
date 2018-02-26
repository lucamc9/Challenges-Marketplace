# from django.db import models
# from django.conf import settings
# from django.db.models.signals import pre_save, post_save
# from profiles.utils import unique_slug_generator
# from django.core.urlresolvers import reverse
#
# User = settings.AUTH_USER_MODEL
#
# class Room(models.Model):
#     user = models.ForeignKey(User)
#     compliance = models.FileField(blank=True, null=True)
#     finance = models.FileField(blank=True, null=True)