#•••••••••••••••••••••••••••••••••#
# ░█▀▀░█▀█░█▀▄░█▄█░█▀▀
# ░█▀▀░█░█░█▀▄░█░█░▀▀█
# ░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀
# Contributor(s): AndrewC,
# Version: 1.0.0
# Homepage: http://bedev.playdate.surge.sh/docs/groups/forms
# Description:Each model that is editable by users needs to have a form that points to that particular model.
#•••••••••••••••••••••••••••••••••#
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models
from events.models import Event as eventModel


class joinGroupForm(ModelForm):
    # This is an empty form and is used only to connect views<->models
    class Meta:
        model = models.Member
        fields = []


class createGroupForm(ModelForm):
    class Meta:
        model = models.Group
        fields = ['group_name', 'group_desc', 'tags', 'banner']
        labels = {
            'group_name': ('Group Name'), 'group_desc': ('Group Description'), 'tags': ("Enter keywords separated by a space; These words will help users to find your group.")
        }
        widgets = {
            'group_name': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "e.g. San Francisco Dog Group"}),
            'group_desc': forms.Textarea(attrs={'style': 'width:65vw;', 'placeholder': "Enter a brief description on what your group is all about!"}),
            'tags': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "dogs, dog, canine, canines, shiba inu, shiba-inu, shiba inu"}),
            # 'banner': forms.ImageField(),

        }


class memberListForm(ModelForm):
    # This is an empty form because users cannot edit the Member table
    class Meta:
        model = models.Member
        fields = []


class createGroupEventForm(ModelForm):
    class Meta:
        model = models.GroupEvent
        fields = ['address', 'desc', 'name', 'banner', 'datetime']
        widgets = {
            'address': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "e.g. 12201 Holloway Ave, San Francisco, CA, 94132"}),
            'desc': forms.Textarea(attrs={'style': 'width:65vw;', 'placeholder': "Enter a brief description on what this event is all about."}),
            'name': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "e.g. Kyle's 12th Birthday Party!"}),
            'datetime': forms.DateInput(attrs={'type': 'date'}),

            # 'banner': forms.ImageField(),

        }


class GroupRSVPForm(ModelForm):
    # This is an empty form because users cannot edit the Member table
    class Meta:
        model = models.RSVP
        fields = []


class createGroupEventCommentForm(ModelForm):
    class Meta:
        model = models.groupEventComment
        fields = ['content', ]
        widgets = {
            'content': forms.Textarea(attrs={'style': 'width: 100%; height:8vh', 'placeholder': "Your comment here."})
        }


class createGroupPostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['post_title', 'post_content', ]
        widgets = {
            'post_title': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "What is your post about?"}),
            'post_content': forms.Textarea(attrs={'style': 'width:65vw;', 'placeholder': "Write your post so other members can see!"}),

        }


class createGroupCommentForm(ModelForm):
    class Meta:
        model = models.groupPostComment
        fields = ['content', ]
        widgets = {
            'content': forms.Textarea(attrs={'style': 'width: 100%; height:8vh', 'placeholder': "Your comment here."})
        }
