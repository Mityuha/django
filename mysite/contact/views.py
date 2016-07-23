#-*- encoding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.contact.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
			request.POST['subject'],
			request.POST['message'],
			request.POST.get('e-mail', 'noreply@example.com'),
			['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial = 
			{'subject':'Мне очень нравится ваш сайт!'})	
	return render_to_response('contact_form.html', {'form': form})

def contact_thanks(request):
	return render_to_response('contact_thanks.html', {})