from django import forms
from .models import DiagnosticsQuestionnaire

class DiagnosticsForm(forms.ModelForm):
    class Meta:
        model = DiagnosticsQuestionnaire
        fields = [
            'organisation',
            'leadership'
        ]
        labels = {
            'organisation': 'sup yo',
            'leadership' : 'ok les go'
        }
        widgets = {
            'organisation' : forms.RadioSelect()
        }