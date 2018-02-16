from django import forms
from .models import DiagnosticsQuestionnaire
from .utils import get_organisation_form_settings

class DiagnosticsForm(forms.ModelForm):
    class Meta:
        model = DiagnosticsQuestionnaire
        fields, labels, widgets = get_organisation_form_settings()