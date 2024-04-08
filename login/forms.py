from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm



class UpdateUser(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ChangePassword(SetPasswordForm):
    class Meta:
        model= User
        fields = ['new_password1', 'new_password2']