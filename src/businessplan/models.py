from django.db import models
from django import forms
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django_countries.fields import CountryField
import datetime
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class BusinessPlan(models.Model):
    user = models.ForeignKey(User)
    model = models.TextField(max_length=1500, blank=True, null=True)
    qualifications = models.CharField(max_length=1500, blank=True, null=True)
    exit = models.CharField(max_length=1500, blank=True, null=True)
    summary = models.CharField(max_length=1500, blank=True, null=True)
    competitors = models.CharField(max_length=1500, blank=True, null=True)
    customers = models.CharField(max_length=1500, blank=True, null=True)
    market = models.CharField(max_length=1500, blank=True, null=True)
    problem = models.CharField(max_length=1500, blank=True, null=True)
    solution = models.CharField(max_length=1500, blank=True, null=True)
    strategy = models.CharField(max_length=1500, blank=True, null=True)
    advantages = models.CharField(max_length=1500, blank=True, null=True)
    financials = models.FileField(blank=True, null=True)
    plan = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('businessplan:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_model(self):
        return self.model

    def get_qualifications(self):
        return self.qualifications

    def get_exit(self):
        return self.exit

    def get_summary(self):
        return self.summary

    def get_competitors(self):
        return self.competitors

    def get_customers(self):
        return self.customers

    def get_market(self):
        return self.market

    def get_problem(self):
        return self.problem

    def get_solution(self):
        return self.solution

    def get_strategy(self):
        return self.strategy

    def get_advantages(self):
        return self.advantages

    def get_financials(self):
        return self.financials
