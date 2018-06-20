# Generated by Django 2.0.6 on 2018-06-17 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('follower', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(blank=True, default='Bangarang!', max_length=100, null=True)),
                ('avatar', models.CharField(default='', max_length=255)),
                ('secondary_email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_profile', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile_data',
            },
        ),
    ]
