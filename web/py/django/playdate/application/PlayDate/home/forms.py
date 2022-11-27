from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class profileForm(ModelForm):
    class Meta:
        model = models.Profile
        #exclude = ('profileDesc', 'avatar',)
        fields = ['profileDesc', 'avatar']
        labels = {
            'profileDesc': ('Profile Description'), 'avatar': ('Avatar'),
        }


class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        model.is_staff = False
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class accountForm(ModelForm):
    class Meta:
        model = models.Account
        fields = ['gender', 'dob']
        labels = {
            'dob': ('D. O. B.'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


class supportForm(ModelForm):
    class Meta:
        model = models.Requestsupport
        fields = ['contact', 'name', 'type', 'details']
        labels = {
            'contact': ('Your Email or Phone'),
            'name': ('Name of the Issue'),
            'type': ('Support Category'),
            'details':  ('Please provide detail of the issue')
        }


class addressForm(ModelForm):
    class Meta:
        model = models.Address
        fields = ['street', 'state', 'country', 'zipcode', 'city']
        labels = {
            'street': ('Street/Building'),
            'state': ('State'),
            'country': ('Country'),
            'zipcode': ('Zipcode'),
            'city': ('City')
        }
