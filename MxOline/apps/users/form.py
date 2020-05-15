from django import forms
from apps.users.confirm import pwd_re


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    password = forms.CharField(required=True, min_length=13)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=2, max_length=13)
    password = forms.CharField(required=True, min_length=6, max_length=13)
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
