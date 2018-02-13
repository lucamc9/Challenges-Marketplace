from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Diagnostics(models.Model):
    user = models.ForeignKey(User)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organisation = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)
    staff = models.IntegerField(null=True, blank=True)
    hr = models.IntegerField(null=True, blank=True)
    facilities = models.IntegerField(null=True, blank=True)
    finance = models.IntegerField(null=True, blank=True)
    manproc = models.IntegerField(null=True, blank=True)
    marketing = models.IntegerField(null=True, blank=True)
    environ = models.IntegerField(null=True, blank=True)
    IT = models.IntegerField(null=True, blank=True)
    legal = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('diagnostics:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_organisation(self):
        return self.organisation

    def get_leadership(self):
        return self.leadership

    def get_staff(self):
        return self.hr

    def get_facilities(self):
        return self.user

    def get_finance(self):
        return self.finance

    def get_manproc(self):
        return self.manproc

    def get_marketing(self):
        return self.marketing

    def get_environ(self):
        return self.environ

    def get_IT(self):
        return self.IT

    def get_legal(self):
        return self.legal

class Diagnostics(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organisation = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_organisation(self):
        return self.organisation

    def get_leadership(self):
        return self.leadership






def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Diagnostics)


