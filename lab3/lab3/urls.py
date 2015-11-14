from django.conf.urls import patterns, include, url
from django.contrib import admin
from ab_bro.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ab_bro/$',ab_bro),
    url(r'^add_author/',add_author),
    url(r'^add_author_success/',add_author_success),
    url(r'^add_book/',add_book),
    url(r'^book_info/(.+)/',book_info),
    url(r'^delete_book/',delete_book),
    url(r'^author_search/',author_search),
    url(r'^show_all/',show_all),
    url(r'^admin/', include(admin.site.urls)),
)
