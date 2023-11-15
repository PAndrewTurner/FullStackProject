from django.db import models
from django.core.exceptions import ValidationError

class CreditProfile(models.Model):
    no_of_dependents = models.IntegerField()
    education = models.CharField(max_length=100)
    self_employed = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_score = models.IntegerField()
    res_assets = models.DecimalField(max_digits=10, decimal_places=2)
    com_assets = models.DecimalField(max_digits=10, decimal_places=2)
    bank_assets = models.DecimalField(max_digits=10, decimal_places=2)
    total_assets = models.DecimalField(max_digits=10, decimal_places=2)
    
