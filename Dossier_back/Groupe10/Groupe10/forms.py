from django import forms
from .models import EmploiTemps

class EmploiTempsForm(forms.ModelForm):
    class Meta:
        model = EmploiTemps
        fields = '__all__'
