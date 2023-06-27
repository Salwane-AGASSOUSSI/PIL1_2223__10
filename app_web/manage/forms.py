
from django import forms
from .models import Utilisateur


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenoms', 'username', 'matricule', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

