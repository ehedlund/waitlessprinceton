from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import docs.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^meettheteam', hello.views.about),
    url(r'^casCGI', hello.views.casCGI),
    url(r'statussite', docs.views.statussite),
    url(r'^admin/', include(admin.site.urls)),
]
