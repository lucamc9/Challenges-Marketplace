from django import forms
from django.contrib.auth import get_user_model
from .models import Compliance, Finance, Legal, Competition
from betterforms.multiform import MultiModelForm
import itertools

User = get_user_model()

class ComplianceForm(forms.ModelForm):
    class Meta:
        model = Compliance
        fields = ('file',)
        widgets = {'file': forms.ClearableFileInput(attrs={'multiple': True})}

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ('file',)
        widgets = {'file': forms.ClearableFileInput(attrs={'multiple': True})}

class LegalForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = ('file',)
        widgets = {'file': forms.ClearableFileInput(attrs={'multiple': True})}

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('file',)
        widgets = {'file': forms.ClearableFileInput(attrs={'multiple': True})}

# class RoomForm(MultiModelForm):
#     form_classes = {
#         'compliance': ComplianceForm,
#         'finance': FinanceForm,
#         'legal': LegalForm,
#         'competition': CompetitionForm
#     }

class RoomForm(forms.Form):
    parent_forms = [ComplianceForm, FinanceForm, LegalForm, CompetitionForm]

    def __init__(self, parent_forms=[], *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        # If the class was instantiated with a list of parent Forms as
        # an argument, use said list. Else look for a hard-coded attribute.
        # This line is hilarious.
        parent_forms = parent_forms if parent_forms else self.parent_forms

        # Make a list of form fields. The list comprehension makes a
        # nested list that gets flattened by itertools' chain
        form_values = list(itertools.chain(
            *[form().fields.items() for form in parent_forms]
        ))
        # Add the values of the parent forms to the actual form
        for k, v in form_values:
            self.fields[k] = v

