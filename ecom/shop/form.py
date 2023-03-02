from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CreateAccount(UserCreationForm):
    first_name =forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    # class meta:
    #     model=Useru
    #     field='__al__'