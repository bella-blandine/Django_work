
from django import forms
from .models import Performance, Audition

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['performer', 'audition', 'score']

class AuditionForm(forms.ModelForm):
    class Meta:
        model = Audition
        fields = ['title', 'description']
