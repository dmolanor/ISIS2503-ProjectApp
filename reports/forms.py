from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'variable',
            'value',
            'unit',
            'place',
            'patient_name',
            'summary',
            'image_url',
            # 'dateTime',  # Si se desea incluir o asignar automáticamente
        ]

        labels = {
            'variable': 'Variable',
            'value': 'Value',
            'unit': 'Unit',
            'place': 'Place',
            'patient_name': 'Patient Name',
            'summary': 'Summary',
            'image_url': 'Image URL',
            # 'dateTime': 'Date Time',
        }
