from django.conf.urls import patterns, include, url

from models import Place 

urlpatterns = patterns('places_app.views',
url(r'^$', 'view'),
url(r'^place/(?P<r_id>d+)/$', 'list_date'),
url(r'^create/$', 'create'),
#url(r'^view/post/(?P<p_id>d+)/$','view', name = 'list_date'),
)

