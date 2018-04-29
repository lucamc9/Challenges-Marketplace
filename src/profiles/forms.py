from django import forms
from django.contrib.auth import get_user_model
from .models import SMEProfile, StaffProfile

User = get_user_model()

class SMEForm(forms.ModelForm):
    class Meta:
        model = SMEProfile
        fields = [
            'user',
            'company_name',
            'description',
            'legal_struct',
            'ownership',
            'country',
            'year',
            'currency',
            'lkin_urls',
            'sector'
        ]

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = [
            'full_name',
            'role'
        ]