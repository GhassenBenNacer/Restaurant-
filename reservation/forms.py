from django import forms
from .models import reserv_model

class reservation_form(forms.ModelForm):
    class Meta:
        model = reserv_model
        fields = "__all__"
        exclude = ['status']
        widgets = {
            'Nom': forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 400px;'}),
            'nbre_person': forms.NumberInput(attrs={'class': 'form-control text-center', 'min': 1, 'style': 'width: 400px;'}),
            'date': forms.DateInput(attrs={'class': 'form-control text-center', 'type': 'date', 'style': 'width: 400px;'}),
            'heure': forms.TimeInput(attrs={'class': 'form-control text-center', 'type': 'time', 'style': 'width: 400px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control text-center', 'style': 'width: 400px;'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 400px;'}),

        }
        labels = {
            'nbre_person': 'Nombre de personnes',
            'Nom': 'Nom & Prénom'
        }



