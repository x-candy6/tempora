# •••••••••••••••••••••••••••
# ░█▄█░█▀█░█▀▄░█▀▀░█░░░█▀▀
# ░█░█░█░█░█░█░█▀▀░█░░░▀▀█
# ░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀

# Contributor(s): AndrewC,
# Version: 1.2.0
# Homepage: http://bedev.playdate.surge.sh/docs/groups/models
# Description: These models reflect group tables and their related entities
# •••••••••••••••••••••••••••
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from events.models import Event


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64, default=None, blank=True)
    group_admin = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    group_desc = models.TextField(
        max_length=512, null=True, blank=True, default=None)

    banner = models.ImageField(
        upload_to="group_banner", default="default.jpeg", blank=True)

    # Django-Taggit: This ties to the Groups and Taggit Tables
    # tags are delimited by commas
    tags = TaggableManager()


class Member(models.Model):
    # Refactor this to Groupuser
    member_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    group_id = models.ForeignKey(
        Group, to_field='group_id', default=None, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('group_id', 'member_id',)
    #isAdmin = models.BooleanField(default=False)


class GroupEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    #address = models.ForeignKey(Address, models.DO_NOTHING)
    address = models.TextField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # backend_admin = models.ForeignKey(
    #    Backendadmin, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)
    # group_admin = models.ForeignKey(
    #    Groupadmin, models.DO_NOTHING, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    datetime = models.DateTimeField(blank=True, null=True)
    banner = models.ImageField(
        upload_to="publicevents_banner", default=None, blank=True)
    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'GroupEvent'


class RSVP(models.Model):
    # Refactor this to Groupuser
    rsvp_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    group_id = models.ForeignKey(
        Group, to_field='group_id', default=None, on_delete=models.CASCADE)
    event_id = models.ForeignKey(
        GroupEvent, default=None, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('group_id', 'rsvp_id', 'event_id',)
        db_table = 'GroupEventRSVP'
    #isAdmin = models.BooleanField(default=False)


class groupEventComment(models.Model):
    # Changed to auto field
    comment_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(
        GroupEvent, on_delete=models.CASCADE, blank=True, null=True)
    #comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'GroupEvent_Comment'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    post_title = models.CharField(max_length=128)
    post_content = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'GroupPost'


class groupPostComment(models.Model):
    # Changed to auto field
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    #comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'GroupPost_Comment'


class Groupadmin(models.Model):
    group_admin_id = models.IntegerField(primary_key=True)
    group_user = models.ForeignKey(Member, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'GroupAdmin'
        unique_together = (('group_admin_id', 'group_user'),)


# The code for Event is already written in events>models.py
# class groupEvent(events.models.Event):

# •••••••••••••••••••••••••••••••••••••••••••••••••••
# ░█▀█░█▀▄░█▀▀░█░█░▀█▀░█░█░█▀▀░█▀▄░░░█▀▀░█▀█░█▀▄░█▀▀
# ░█▀█░█▀▄░█░░░█▀█░░█░░▀▄▀░█▀▀░█░█░░░█░░░█░█░█░█░█▀▀
# ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀░░░░▀▀▀░▀▀▀░▀▀░░▀▀▀
# •••••••••••••••••••••••••••••••••••••••••••••••••••

# JoinGroup is a view function not a model class
# class Joingroup(models.Model):
#    join_group_id = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User, models.DO_NOTHING)
#    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
#    datetime = models.DateTimeField()
#
#    class Meta:
#        # managed = False
#        db_table = 'JoinGroup'
#
#
# ManageGroupUser is a view function not a model class
# class Managegroupuser(models.Model):
#    manage_id = models.IntegerField(primary_key=True)
#    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING, blank=True, null=True)
#    join_group = models.ForeignKey(Joingroup, models.DO_NOTHING, blank=True, null=True)
#    operation = models.CharField(max_length=45)
#
#    class Meta:
#        # managed = False
#        db_table = 'ManageGroupUser'
#
# class Group(models.Model):
#    group_id = models.IntegerField(primary_key=True)
#    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING)
#    group_name = models.CharField(max_length=45)
#    group_desc = models.CharField(max_length=200)
#    create_date = models.DateTimeField()
#    group_size = models.IntegerField()
#
#    class Meta:
#        db_table = 'Group'


# class Groupuser(models.Model):
# Already implemented under 'Member'
# This is equivalent to Member
#    group_user_id = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User, models.DO_NOTHING)
#
#    class Meta:
#        # managed = False
#        db_table = 'GroupUser'
#        unique_together = (('group_user_id', 'user'),)
