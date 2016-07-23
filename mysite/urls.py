from django.conf.urls.defaults import patterns, include, url
#from mysite.views import *
#from mysite.books import views
#from mysite.contact.views import contact, contact_thanks
# Uncomment the next two lines to enable the admin:
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from mysite.books.models import Publisher
from django.views.generic import list_detail 
admin.autodiscover()

from mysite.blog.feeds import LatestEntries #, LatestEntriesByCategory

publisher_info = {'queryset': Publisher.objects.all(),
		'template_name': 'publisher_list_page.html',
		'template_object_name': 'publisher',}

urlpatterns = patterns('',
	("^hello/$", 'mysite.views.hello'),
	("^$", 'mysite.views.home_page'),#home page
	("^time/$", 'mysite.views.current_datetime'),
	(r"^time/plus/(\d{1,2})/$", 'mysite.views.hour_ahead'),
	(r"^request/$", 'mysite.views.display_meta'),
	(r"^search/$", 'mysite.books.views.search'),
	(r"^contact/$", 'mysite.contact.views.contact'),
	(r"^contact/thanks/$", 'mysite.contact.views.contact_thanks'),
	(r'^about/$', direct_to_template, {'template':'about.html'}),
	(r'^about/(\w+)/$', 'mysite.books.views.about_pages'),
	(r'^publishers/$', list_detail.object_list, publisher_info),
	('^books/([A-Za-z0-9\']+)/$', "mysite.books.views.books_by_publisher"),
	(r'^books/authors_list', "mysite.books.views.authors_list_plaintext"),
	url(r'^feeds/latest/', LatestEntries()),
	url(r'^comment/(?P<object_pk>\w+)/', 'mysite.blog.views.comment'),
	(r'^accounts/login/$', login, {'template_name':'login.html'}),
	(r'^accounts/logout/$', logout),
	(r'^accounts/register/$', 'mysite.views.register'),
	#(r'^.*', direct_to_template, {'template': '404.html'}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
