from django import forms
from django.shortcuts import render
from .models import CreditProfile
from django.core.exceptions import ValidationError

class CreditProfileForm(forms.ModelForm):
    class Meta:
        model = CreditProfile
        fields = ['no_of_dependents', 'education', 'self_employed', 'annual_income', 'loan_amount', 'credit_score', 'res_assets', 'com_assets', 'bank_assets', 'total_assets']
    


