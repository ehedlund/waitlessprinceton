from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/hello/favicon.ico', permanent=True)

urlpatterns = patterns(
    url(r'^favicon\.ico$', favicon_view)
)
