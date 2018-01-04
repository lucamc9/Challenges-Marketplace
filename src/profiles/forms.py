from django import forms
from django.contrib.auth import get_user_model
from .models import SMEProfile

User = get_user_model()

class SMEForm(forms.ModelForm):
    class Meta:
        model = SMEProfile
        fields = [
            'description',
            'legal_struct',
            'ownership',
            'country',
            'year',
            'currency',
            'lkin_urls',
            'sector'
        ]