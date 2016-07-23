#-*- encoding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailField(required=False, label="e-mail")
	message = forms.CharField(widget=forms.Textarea)
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Too few words (<4)!")
		return message
