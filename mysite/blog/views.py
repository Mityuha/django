from mysite.blog.models import Entry
from django.http import HttpResponse

def comment(request, object_pk):
	mycomment = Entry.objects.get(id = object_pk)
	text = ('<strong>Title :</strong> %s <p>' % mycomment.title ) + '</p>'
	text += ('<strong>Description :</strong> %s <p>' % mycomment.description ) + '</p>'
	text += ('<strong>Link :</strong> {%url mysite.blog.views.comment %} <p>') + '</p>'
	return HttpResponse(text)
