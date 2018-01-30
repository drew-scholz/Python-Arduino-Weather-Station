# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Wind(models.Model):
	speed = models.CharField(max_length=3)
	direction = models.CharField(max_length=2)
	stationID = models.CharField(max_length=20, default='new_station')
	
	def __str__(self):
		return self.speed
	