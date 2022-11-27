# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.


# class Address(models.Model):
#     address_id = models.IntegerField(primary_key=True)
#     street = models.CharField(max_length=45)
#     country = models.CharField(max_length=20)
#     city = models.CharField(max_length=45)
#     zipcode = models.IntegerField()

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=100, default='NA')
    country = models.CharField(max_length=20, default='NA')
    city = models.CharField(max_length=45, default='NA')
    zipcode = models.IntegerField(default=00000)
    state = models.CharField(max_length=45, default='NA')

    class Meta:
        db_table = 'Address'


class generalUser(models.Model):
    trackingID = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=50)

    class Meta:
        db_table = 'generalUser'


class Account(models.Model):
    gender_choices = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('NON_BINARY', 'Non-Binary'),
    ]
    #accountID = models.AutoField(primary_key=True)
    accountID = models.ForeignKey(
        User, default=None, unique=True, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(
        max_length=10, choices=gender_choices)
    # fname=models.CharField(max_length = 30)
    # lname=models.CharField(max_length = 30)
    dob = models.DateField(max_length=11)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Account'


class Profile(models.Model):
    profileID = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, primary_key=True)
    profileDesc = models.TextField(
        max_length=256, null=True, blank=True, default=None)
    avatar = models.ImageField(
        upload_to="uploads", default=None, blank=True)
    address = models.ForeignKey(
        Address, null=True, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        db_table = 'Profile'


class Backendadmin(models.Model):
    backend_admin_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'BackendAdmin'
        unique_together = (('backend_admin_id', 'user'),)


class Dependent(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey('Profile', models.DO_NOTHING)
    name = models.CharField(max_length=45)
    dob = models.DateTimeField()
    interests = models.CharField(max_length=45)

    class Meta:
        # managed = False
        db_table = 'Dependent'


class Requestsupport(models.Model):
    SUPPORT_TYPE_REPORT = "REP"
    SUPPORT_TYPE_ONBOARD = "ONB"
    SUPPORT_TYPE_BUG = "BUG"
    SUPPORT_TYPE_OTHER = "OTH"
    SUPPORT_TYPE_CHOICES = [
        (SUPPORT_TYPE_REPORT, "Report User or Content"),
        (SUPPORT_TYPE_ONBOARD, "Registration Issues"),
        (SUPPORT_TYPE_BUG, "PlayDate Not Working"),
        (SUPPORT_TYPE_OTHER, "Other")
    ]
    request_id = models.AutoField(primary_key=True)
    accountID = models.ForeignKey(
        User, models.DO_NOTHING, blank=True, null=True)
    general = models.ForeignKey(
        generalUser, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(
        'Supportstaff', models.DO_NOTHING, blank=True, null=True)
    contact = models.CharField(max_length=52)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    type = models.CharField(
        max_length=3, choices=SUPPORT_TYPE_CHOICES, default=SUPPORT_TYPE_ONBOARD)
    details = models.TextField(max_length=500)

    class Meta:
        # managed = False
        db_table = 'RequestSupport'


class Supportstaff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_email = models.CharField(max_length=45)

    class Meta:
        # managed = False
        db_table = 'SupportStaff'


class Friendlist(models.Model):
    friend_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'FriendList'
