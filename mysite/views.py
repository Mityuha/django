from django.shortcuts import render_to_response
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def hello(request):
	return HttpResponse("Hello world")

def home_page(request):
	return HttpResponse("Home page!")

def current_datetime(request):
	return render_to_response("current_datetime.html", {'current_date':datetime.datetime.now()})

@login_required
def display_meta(request):
	values = request.META.items()
	values.append(('request_path', request.path))
	values.append(('request_get_host', request.get_host()))
	values.append(('request_get_full_path', request.get_full_path()))
	values.append(('request_is_secure', request.is_secure()))
	for k,v in request.session.items():
		values.append((k, v))
	values.sort()
	return render_to_response("display_meta.html", {'request_items':values,})

def hour_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	return render_to_response("hour_ahead.html", 
	{'hour_offset': offset, 
	'next_time': datetime.datetime.now()+datetime.timedelta(hours=offset),
	'current_datetime':datetime.datetime.now()})

def search_form(request):
	return render_to_response("search_form.html", {})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/about/')
	else:
		form = UserCreationForm()
	return render_to_response('registration/register.html', {'form':form,})
