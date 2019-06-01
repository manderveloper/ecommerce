from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.Form, UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                help_text = self.fields[field].help_text
                self.fields[field].help_text = None
                if help_text != '':
                    self.fields[field].widget.attrs.update(
                        {'class': 'has-popover', 'data-content': help_text, 'data-placement': 'right',
                         'data-container': 'body'})

        def save(self, commit=True):
            user = super(ProfileForm, self).save(commit=False)
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
