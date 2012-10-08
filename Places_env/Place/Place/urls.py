from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('Place_app.views',
    url(r'^$', 'index'),
    url(r'^list_date/$', 'list_date'),  # List places descending date 
    url(r'^list_view/$', 'list_nr_views'),  # List places by number of views
    url(r'^place/(\d{1,2})/$', 'detail'),  # Detail of the place
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
