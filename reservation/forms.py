from django import forms
from .models import reserv_model

class reservation_form(forms.ModelForm):
  class Meta:
    model = reserv_model
    fields = "__all__"
    exclude = ['status']
    widgets = {
      'Nom': forms.TextInput(attrs={'class': 'form-control'}),
      'nbre_person': forms.NumberInput(attrs={'class': 'form-control'}),
      'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'heure': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'telephone': forms.TextInput(attrs={'class': 'form-control'}),
    }
    labels = {
      'nbre_person': 'Nombre de personnes',
      'Nom': 'Nom & Prénom'
    }



