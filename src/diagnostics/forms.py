from django import forms
from .models import DiagnosticsRaw

class DiagnosticsForm(forms.ModelForm):
    class Meta:
        model = DiagnosticsRaw
        fields = [
            'plan',
            'model',
            'qualifications',
            'exit',
            'summary',
            'competitors',
            'customers',
            'market',
            'problem',
            'solution',
            'strategy',
            'advantages',
            'financials'
        ]
        labels = {
            'model': 'What is your business model?',
            'plan': 'Upload your business plan',
            'qualifications': 'What management qualifications do you and your team have as related to this venture?',
            'exit': 'Describe your exit strategy',
            'summary': 'Summarise your business',
            'competitors': 'List your competitors',
            'customers': 'List your specific current or potential customers',
            'market': 'Size your potential market of customers',
            'problem': 'What is the customer problem your product is solving?',
            'solution': 'What is your solution?',
            'strategy': 'Describe your "go-to-market" and sales strategy',
            'advantages': 'Describe your competitive advantage and barriers to entry',
            'financials': 'Financials - Revenues, expenditures and net income for the last 2 years and next 3 years projected'
        }