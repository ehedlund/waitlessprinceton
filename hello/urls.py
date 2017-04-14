from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
import views

admin.autodiscover()


# Authentication urls
urlpatterns = patterns('django_cas.views',
    (r'^login/?$', 'login'),
    (r'^logout/?$', 'logout'),
)

# Normal urls
urlpatterns += patterns('rooms.views',
    (r'^$', 'index'),
    (r'^about', 'about'),
    (r'^statussite', 'statussite'),
    (r'^test', 'index'),
    url(r'^admin/', include(admin.site.urls)),
)
