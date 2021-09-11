from django import forms
from django.forms import fields
from .models import Bills


class BillsModelForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = (
            'name',
            'amount',
            'dueDate',
            'automaticPayment',
            'payd',
            'info',
        )

class billsForm(forms.Form):
    name = forms.CharField()
    amount = forms.FloatField()
    dueDate = forms.IntegerField(min_value=1, max_value=20)
    automaticPayment = forms.BooleanField()
    payd = forms.BooleanField()