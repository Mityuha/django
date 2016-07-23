#-*- encoding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from mysite.blog.models import Entry
from mysite.blog.views import comment
from django.contrib.comments import Comment

class LatestEntries(Feed):
	
	title = "Мой блог"
	link = "/"
	description = "Последние новости по теме."
	
	def items(self):
		return Entry.objects.order_by('-pub_date')
	
	def item_title(self, item):
        	return item.title

	def item_description(self, item):
        	return item.description
	
	def item_link(self, item):
		return reverse('mysite.blog.views.comment', kwargs={'object_pk':item.pk})
