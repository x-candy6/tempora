# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.IntegerField(primary_key=True)
    general = models.ForeignKey('Generaluser', models.DO_NOTHING)
    gender = models.CharField(max_length=6)
    is_varified = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Account'
        unique_together = (('account_id', 'general'),)


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=45)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Address'


class Authuser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    general = models.ForeignKey('Generaluser', models.DO_NOTHING)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    is_active = models.TextField()  # This field type is a guess.
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    is_supervisor = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AuthUser'
        unique_together = (('user_id', 'general', 'email'),)


class Backendadmin(models.Model):
    backend_admin_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BackendAdmin'
        unique_together = (('backend_admin_id', 'user'),)


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    datetime = models.DateTimeField()
    content = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Comment'


class Dependent(models.Model):
    dependent_id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey('Profile', models.DO_NOTHING)
    name = models.CharField(max_length=45)
    dob = models.DateTimeField()
    interests = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Dependent'


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING)
    backend_admin = models.ForeignKey(Backendadmin, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey('Group', models.DO_NOTHING, blank=True, null=True)
    group_admin = models.ForeignKey('Groupadmin', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Event'


class Friendlist(models.Model):
    friend_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'FriendList'


class Generaluser(models.Model):
    general_id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'GeneralUser'


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_admin = models.ForeignKey('Groupadmin', models.DO_NOTHING)
    group_name = models.CharField(max_length=45)
    group_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    group_size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Group'


class Groupadmin(models.Model):
    group_admin_id = models.IntegerField(primary_key=True)
    group_user = models.ForeignKey('Groupuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'GroupAdmin'
        unique_together = (('group_admin_id', 'group_user'),)


class Groupuser(models.Model):
    group_user_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'GroupUser'
        unique_together = (('group_user_id', 'user'),)


class Joingroup(models.Model):
    join_group_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'JoinGroup'


class Managegroupuser(models.Model):
    manage_id = models.IntegerField(primary_key=True)
    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING, blank=True, null=True)
    join_group = models.ForeignKey(Joingroup, models.DO_NOTHING, blank=True, null=True)
    operation = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ManageGroupUser'


class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    photo_path = models.CharField(max_length=100)
    desciption = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Profile'


class Publicevent(models.Model):
    public_event_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    event_url = models.CharField(max_length=100)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'PublicEvent'


class Requestsupport(models.Model):
    request_id = models.IntegerField(primary_key=True)
    general = models.ForeignKey(Generaluser, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('Supportstaff', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=10)
    details = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'RequestSupport'


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Role'


class Signup(models.Model):
    signup_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'SignUp'


class Supportstaff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'SupportStaff'


class Survey(models.Model):
    survey_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Authuser, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Survey'


class Userole(models.Model):
    use_role_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(Account, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UseRole'
