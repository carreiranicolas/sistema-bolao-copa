from django import forms
from .models import Palpite

class PalpiteForm(forms.ModelForm):
    class Meta:
        model = Palpite
        fields = ['gols_casa', 'gols_fora']

        widgets = {
            'gols_casa': forms.NumberInput(
                attrs={
                    'class': 'form-control text-center fw-bold fs-4',
                    'min': 0,
                }
            ),
            'gols_fora': forms.NumberInput(
                attrs={
                    'class': 'form-control text-center fw-bold fs-4',
                    'min': 0,
                }
            ),
        }