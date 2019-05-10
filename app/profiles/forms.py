from django import forms

from .models import Profiles


class ProfileForm(forms.Form):
    username    = forms.CharField()
    email       = forms.EmailField()
    password    = forms.CharField(widget=forms.PasswordInput)




