# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiledata',
            name='avatar',
            field=models.CharField(default='https://imgur.com/jVr43h8.png', max_length=255),
        ),
    ]
