from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL


class Compliance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='compliance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_file(self):
        return self.file

    def get_parent(self):
        return 'Finance & Legal'

class Finance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='finance/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_file(self):
        return self.file

    def get_parent(self):
        return 'Finance & Legal'

class Legal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='legal/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_file(self):
        return self.file

    def get_parent(self):
        return 'Finance & Legal'


class Competition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='competition/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_file(self):
        return self.file

    def get_parent(self):
        return 'Sales & Marketing'

#
# class Room(models.Model):
#     user = models.ForeignKey(User)
#     compliance = models.ForeignKey(Compliance)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def get_absolute_url(self):
#         return reverse('room:detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-updated', '-timestamp']
#
#     def get_user(self):
#         return self.user
#
#     def get_operations(self):
#         return self.operations
#
#     def get_finance(self):
#         return self.finance
#
#     def get_organisation(self):
#         return self.organisation

