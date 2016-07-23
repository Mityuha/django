#-*- coding: utf-8 -*-
from django.db import models


#класс издательства
#описывает соответствующую таблицу в БД
#с полями, являющимися полями класса

class DahlManager(models.Manager):
	def get_query_set(self):
		return super(DahlManager, self).get_query_set().filter(author='Roald Dahl')

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	def __unicode__(self):
		return self.name

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name,)
	

class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	
	objects = models.Manager()
	dahl_objects = DahlManager()

	def __unicode__(self):
		return self.name
	
# Create your models here.
