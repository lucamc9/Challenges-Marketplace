from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.core.urlresolvers import reverse
from django import forms
from django.core import checks, exceptions, validators
from django.db import connection, connections, router
from django.utils.functional import Promise, cached_property, curry


User = settings.AUTH_USER_MODEL

# class IntegerRadioField(models.IntegerField):
#     description = "Integer with Radio widget"
#
#     def get_internal_type(self):
#         return "IntegerRadioField"
#
#     def formfield(self, **kwargs):
#         defaults = {'form_class': forms.ChoiceField(widget=forms.RadioSelect)}
#         defaults.update(kwargs)
#         return super(IntegerRadioField, self).formfield(**defaults)

# class IntegerRadioField(models.Field):
#     empty_strings_allowed = False
#     # default_error_messages = {
#     #     'invalid': _("'%(value)s' value must be an integer."),
#     # }
#     description = "Integer Radio Field"
#
#     def check(self, **kwargs):
#         errors = super(IntegerRadioField, self).check(**kwargs)
#         errors.extend(self._check_max_length_warning())
#         return errors
#
#     def _check_max_length_warning(self):
#         if self.max_length is not None:
#             return [
#                 checks.Warning(
#                     "'max_length' is ignored when used with IntegerField",
#                     hint="Remove 'max_length' from field",
#                     obj=self,
#                     id='fields.W122',
#                 )
#             ]
#         return []
#
#     @cached_property
#     def validators(self):
#         # These validators can't be added at field initialization time since
#         # they're based on values retrieved from `connection`.
#         validators_ = super(IntegerRadioField, self).validators
#         internal_type = self.get_internal_type()
#         min_value, max_value = connection.ops.integer_field_range(internal_type)
#         if min_value is not None:
#             for validator in validators_:
#                 if isinstance(validator, validators.MinValueValidator) and validator.limit_value >= min_value:
#                     break
#             else:
#                 validators_.append(validators.MinValueValidator(min_value))
#         if max_value is not None:
#             for validator in validators_:
#                 if isinstance(validator, validators.MaxValueValidator) and validator.limit_value <= max_value:
#                     break
#             else:
#                 validators_.append(validators.MaxValueValidator(max_value))
#         return validators_
#
#     def get_prep_value(self, value):
#         value = super(IntegerRadioField, self).get_prep_value(value)
#         if value is None:
#             return None
#         return int(value)
#
#     def get_internal_type(self):
#         return "IntegerRadioField"
#
#     def to_python(self, value):
#         if value is None:
#             return value
#         try:
#             return int(value)
#         except (TypeError, ValueError):
#             raise exceptions.ValidationError(
#                 self.error_messages['invalid'],
#                 code='invalid',
#                 params={'value': value},
#             )
#
#     def formfield(self, **kwargs):
#         defaults = {'form_class': forms.ChoiceField(widget=forms.RadioSelect())}
#         defaults.update(kwargs)
#         return super(IntegerRadioField, self).formfield(**defaults)

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
    ORG = (
        (1, 'Equity'),
        (2, 'Trade'),
        (3, 'Debt')
    )
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organisation = models.IntegerField(choices=ORG, default=0)
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

# def pre_save_receiver(sender, instance, *args, **kwargs):
#     # Function to calculate Diagnostics scores from the questionnaire
#     diagnostics = Diagnostics()

pre_save.connect(pre_save_receiver, sender=Diagnostics)
# pre_save.connect(calculate_scores, sender=DiagnosticsQuestionnaire)



