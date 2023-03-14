from django import forms
from .models import Address
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

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'