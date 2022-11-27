# ░█▀▀░█▀█░█▀▄░█▄█░█▀▀
# ░█▀▀░█░█░█▀▄░█░█░▀▀█
# ░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀
from django import forms

CHOICES = [
    ('All', 'All'),
    ('Pets', 'Pets'),
    ('Kids', 'Kids'),
]


class UserForm(forms.Form):
    search = forms.CharField(max_length=100)
    filter = forms.IntegerField(widget=forms.Select(choices=CHOICES))
    # forms.ChoiceField(choices=CHOICES))
