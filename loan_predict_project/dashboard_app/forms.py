from dataclasses import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['client_name', 'gender', 'mstatus',  'dependance',  'education', 'self_employed', 'appIncome', 'co_appIncome', 'loan_amount', 'loan_amount_term', 'credit_history', 'property_area']