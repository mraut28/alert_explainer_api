from django import forms

from .models import Alert


class AlertCreateForm(forms.Form):
    title = forms.CharField(strip=False)
    severity = forms.ChoiceField(choices=Alert.SEVERITY_CHOICES)
    source = forms.CharField(strip=False)
    metric_name = forms.CharField(strip=False)
    metric_value = forms.FloatField()
    threshold = forms.FloatField()