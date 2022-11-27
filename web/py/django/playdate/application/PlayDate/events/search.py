from django import forms

CHOICES= [
    ('All', 'All'),
    ('Pets', 'Pets'),
    ('Kids', 'Kids'),
    ]

class UserForm(forms.Form):
    search= forms.CharField(max_length=100)
    filter= forms.CharField(widget=forms.Select(choices=CHOICES))