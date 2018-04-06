from django.db import models
from django.conf import settings
from profiles.utils import sme_choices
import datetime
from .utils import get_month_choices
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class GraphData(models.Model):
    _, _, YEAR_CHOICES, _, _ = sme_choices()
    MONTHS = get_month_choices()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gross = models.IntegerField(null=True, blank=True)
    net = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    revenues = models.IntegerField(null=True, blank=True)
    expenditures = models.IntegerField(null=True, blank=True)
    cash_flow = models.IntegerField(null=True, blank=True)
    flow_month = models.CharField(max_length=50, choices=MONTHS)

    def get_absolute_url(self):
        return reverse('kpi:demo')

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

    def get_revenues(self):
        return self.revenues

    def get_expenditures(self):
        return self.expenditures

    def get_cash_flow(self):
        return self.cash_flow

    def get_flow_month(self):
        return self.flow_month

class ExcelTemplate(models.Model):
    user = models.ForeignKey(User)
    template = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('kpi:demo')

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_user(self):
        return self.user

    def get_template(self):
        return self.template
