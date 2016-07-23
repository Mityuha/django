#-*- encoding: utf-8 -*-
from django.db import models

class Entry(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	link = models.URLField()
	pub_date = models.DateField()
	def __unicode__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	link = models.URLField()
	tag = models.CharField(max_length=30)
	def __unicode__(self):
		return self.title

