from django import forms
from .models import Contract

class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'contract_title',
            'contract_description',
            'contract_location',
            'contract_salary',
            'contract_recruiter',
            'recruiter_email',
            'recruiter_telephone',
        ]

class ContractUpgradeForm():
    pass

# class ContractEditForm():
#     pass

# class ContractDeletionForm():
#     pass
