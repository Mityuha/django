from django.contrib import admin
from mysite.blog.models import Entry, Tag

class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'link','pub_date')

#class TagAdmin(admin.ModelAdmin):
#	list_display = ('title', 'description', 'link','tag',)
#	list_filter = ('tag',)

admin.site.register(Tag)
admin.site.register(Entry, EntryAdmin)

