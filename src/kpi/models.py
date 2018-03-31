from django.db import models
from django.conf import settings
from profiles.utils import sme_choices
import datetime

User = settings.AUTH_USER_MODEL

class GrossAndNet(models.Model):
    _, _, YEAR_CHOICES, _, _ = sme_choices()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gross = models.IntegerField(null=True, blank=True)
    net = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_user(self):
        return self.user

    def get_gross(self):
        return self.gross

    def get_net(self):
        return self.net

    def get_year(self):
        return self.year