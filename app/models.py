# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    dob= models.CharField(max_length=200)
    aadhar=models.CharField(max_length=200,unique=True)
    area=models.CharField(max_length=200)
    wallet=models.CharField(max_length=200)
