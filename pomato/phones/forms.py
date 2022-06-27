from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from .models import *
from django.contrib.auth.models import User


class UserRegisterModelForm(forms.ModelForm):

    confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm']

        widgets = {
            'password': forms.PasswordInput(),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }