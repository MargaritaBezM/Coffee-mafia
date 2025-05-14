from django import forms
from .models import VacancyPersonModel

class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyPersonModel
        fields = ['name', 'phone', 'email', 'vacancy', 'resume', 'position_text']
        widgets = {
            'vacancy': forms.HiddenInput(),
            'position_text': forms.HiddenInput()
        }