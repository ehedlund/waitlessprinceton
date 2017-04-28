from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import django_cas_ng.views

urlpatterns = [
    url(r'accounts/login/$', django_cas_ng.views.login),
    url(r'accounts/logout/$', django_cas_ng.views.logout),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db$', hello.views.db, name='db'),
    url(r'^about$', hello.views.about,name='about'),
    url(r'^status$', hello.views.status, name='status'),
    url(r'^admin/$', include(admin.site.urls)),
]
