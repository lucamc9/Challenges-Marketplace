from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.core.urlresolvers import reverse
from .utils import get_organisation_questions


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

class DiagnosticsQuestionnaire(models.Model):
    # Retrieve questions
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15 = get_organisation_questions()
    # Standard models
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Organisation questions
    org_1 = models.IntegerField(choices=_1, default=1)
    org_2 = models.IntegerField(choices=_2, default=1)
    org_3 = models.IntegerField(choices=_3, default=1)
    org_4 = models.IntegerField(choices=_4, default=1)
    org_5 = models.IntegerField(choices=_5, default=1)
    org_6 = models.IntegerField(choices=_6, default=1)
    org_7 = models.IntegerField(choices=_7, default=1)
    org_8 = models.IntegerField(choices=_8, default=1)
    org_9 = models.IntegerField(choices=_9, default=1)
    org_10 = models.IntegerField(choices=_10, default=1)
    org_11 = models.IntegerField(choices=_11, default=1)
    org_12 = models.IntegerField(choices=_12, default=1)
    org_13 = models.IntegerField(choices=_13, default=1)
    org_14 = models.IntegerField(choices=_14, default=1)
    org_15 = models.IntegerField(choices=_15, default=1)
    orgs = [org_1, org_2, org_3, org_4, org_5, org_6, org_7, org_8, org_9, org_10, org_11, org_12, org_13, org_14, org_15]
    # Leadership questions

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_organisation(self):
        return self.orgs



def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def pre_save_receiver(sender, instance, *args, **kwargs):
#     # Function to calculate Diagnostics scores from the questionnaire
#     diagnostics = Diagnostics()

pre_save.connect(pre_save_receiver, sender=Diagnostics)
# pre_save.connect(calculate_scores, sender=DiagnosticsQuestionnaire)



