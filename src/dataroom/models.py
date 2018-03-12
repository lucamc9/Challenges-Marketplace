from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class ComplianceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class EnvironmentalModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class FinanceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class LegalModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class CompanyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class GovernanceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class FacilitiesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class TechnologyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class ProcessesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class ProcurementModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class OrganisationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class StaffModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class CompetitionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label


class MarketingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label
