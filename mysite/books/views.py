#-*- encoding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import list_detail
from django.http import HttpResponse
#Модель
from mysite.books.models import Book, Publisher, Author
#

from django.views.generic.simple import direct_to_template
from django.http import Http404
from django.template import TemplateDoesNotExist

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Введите поисковый запрос')
		elif len(q) > 20:
			errors.append('Запрос должен содержать не более 20 символов')
		else:
			#Получить все книги, название которых содержит q без учета регистра
			books = Book.objects.filter(name__icontains=q)#'like' in sql
			return render_to_response('search_results.html',
			{'books': books, 'query': q, })
	return render_to_response('search_form.html',
		{'errors': errors})

def about_pages(request, page):
	try:
		return direct_to_template(request, template="%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()

#Обертка object_list
def books_by_publisher(request, name):
	#Найти издательство (если не найдено, возбудить ошибку 404)
	publisher = get_object_or_404(Publisher, name__iexact=name)
		
	#Основная работа выполняется представлением object_list
	#Результат выполнения Book.objects.filter(...)
	#Будет доступен по переменной template_object_name (т.е. publisher_list)
	return list_detail.object_list(
	request,
	queryset = Book.objects.filter(publisher=publisher),
	template_name = 'books_by_publisher.html',
	template_object_name = 'publisher',
	#В extra_context передается дополнительная информация,
	#в данном случае об издательстве
	extra_context = {'publisher': publisher}
	)

#Сохранить список авторов документом authors.txt
def authors_list_plaintext(request):
	response = list_detail.object_list(
	request, 
	queryset = Author.objects.all(),
	mimetype = 'text/plain',
	template_name = 'author_list.txt'#скорее всего, этот файл можно динамически создать
	)
	#Заголовок Content-Disposition говорит браузеру о том, что файл нужно загрузить
	#и сохранить, а не отображать
	response["Content-Disposition"] = "attachment: filename=authors.txt"
	return response
