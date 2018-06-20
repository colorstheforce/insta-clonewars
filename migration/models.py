# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PostsComments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    comment = models.TextField()
    posted_on = models.DateTimeField()
    image = models.ForeignKey('PostsPost', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_comments'


class PostsPhotolikes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    postid = models.IntegerField()
    liker = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'posts_photolikes'


class PostsPhototag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    photoid = models.IntegerField()
    coords = models.CharField(max_length=20)
    tagged_user = models.CharField(max_length=20)
    tagged_by = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'posts_phototag'


class PostsPost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=60, blank=True, null=True)
    time_created = models.DateTimeField()
    time_updated = models.DateTimeField()
    baseurl = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField()
    owner = models.CharField(max_length=20)
    likes = models.IntegerField()
    caption = models.CharField(max_length=140)
    tags = models.IntegerField()
    main_colour = models.CharField(max_length=15)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts_post'


class RegistrationRegistrationprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    activation_key = models.CharField(max_length=40)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class UserProfileData(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.TextField(blank=True, null=True)
    secondary_email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, unique=True)
    avatar = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_profile_data'


class UserProfileDataFollowers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userprofiledata = models.ForeignKey(UserProfileData, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_data_followers'
        unique_together = (('userprofiledata', 'user'),)


class UserProfileDataFollowing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userprofiledata = models.ForeignKey(UserProfileData, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_data_following'
        unique_together = (('userprofiledata', 'user'),)


class UserprofileFollowers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.CharField(max_length=20)
    follower = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'userprofile_followers'
