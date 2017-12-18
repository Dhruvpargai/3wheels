# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('aadhar', models.IntegerField(unique=True)),
                ('area', models.CharField(max_length=200)),
                ('wallet', models.IntegerField()),
            ],
        ),
    ]
