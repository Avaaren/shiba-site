from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_repeat_password(self):
        cd = self.cleaned_data

        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['repeat_password']