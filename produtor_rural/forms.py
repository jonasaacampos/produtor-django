from django import forms
from .models import Fazenda

class FazendaForm(forms.ModelForm):
    culturas = forms.MultipleChoiceField(
        choices=Fazenda.CULTURAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Fazenda
        fields = '__all__'

    def clean_culturas(self):
        return ','.join(self.cleaned_data['culturas'])