from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from . import views
from django.conf.urls import url

admin.autodiscover()


# Authentication urls
# urlpatterns = patterns('django_cas.views',
#     (r'^login/?$', 'login'),
#     (r'^logout/?$', 'logout'),
# )

# Normal urls
# urlpatterns += patterns('rooms.views',
#     (r'^$', 'index'),
#     (r'^about', 'about'),
#     (r'^statussite', 'statussite'),
#     (r'^test', 'index'),
#     url(r'^admin/', include(admin.site.urls)),
# )

#urlpatterns = [
 #   url(r'^$', views.index),
  #  url(r'^about', views.about),
   # url(r'^casCGI', views.casCGI)
#]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about,name='about'),
    url(r'^casCGI/$', views.casCGI,name='casCGI'),
]
