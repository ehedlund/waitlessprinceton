from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
#import docs
import django_cas_ng.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'accounts/login/$', django_cas_ng.views.login),
    url(r'accounts/logout/$', django_cas_ng.views.logout),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    #url(r'^about/$', hello.views.about,name='about'),
    #url(r'^meet/$', hello.views.meet,name='meet'),
    #url(r'^casCGI/$', hello.views.casCGI,name='casCGI')
    #url(r'^meet', hello.views.about),
    #url(r'^casCGI', hello.views.casCGI),
    #url(r'statussite', docs.views.statussite),
    url(r'^admin/$', include(admin.site.urls)),
]
