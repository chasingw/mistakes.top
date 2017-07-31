# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BeachInfo(models.Model):
    ipaddress = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    come_time = models.DateField()
    nick_name = models.CharField(max_length=128)

#    def __str__(self):
#	return self.ipaddress
