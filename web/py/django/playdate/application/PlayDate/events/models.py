# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from groups.models import Group, Groupadmin
from home.models import Address, Backendadmin
# from django.contrib.gis.db import models as geomodels


# for general users
class Publicevent(models.Model):
    public_event_id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    name = models.CharField(max_length=500)

    banner = models.ImageField(
        upload_to="publicevents_banner", default=None, blank=True)
    # geometry= geomodels.PointField()

    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'PublicEvent'


class Location(models.Model):
    country_code = models.TextField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_code = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Location'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    backend_admin = models.ForeignKey(
        Backendadmin, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
    group_admin = models.ForeignKey(
        Groupadmin, models.DO_NOTHING, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    banner = models.ImageField(upload_to="publicevents_banner", default=None, blank=True)
    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Event'


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    datetime = models.DateTimeField()
    content = models.CharField(max_length=200)

    class Meta:
        # managed = False
        db_table = 'Comment'
