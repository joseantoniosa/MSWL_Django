from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Place_app.views',
    url(r'^$', 'index'),
    url(r'^list_date/$', 'list_date'),  # List places descending date 
    url(r'^list_view/$', 'list_nr_views'),  # List places by number of views
    url(r'^place/(\d{1,2})/$', 'detail'),
#    url(r'^place/(?P<r_id>d+)/$', 'list_date'),

    ## url(r'^place/(?P<r_id>d+)/$', 'list_date'),
    url(r'^create/$', 'create'),
    #url(r'^view/post/(?P<p_id>d+)/$','view', name = 'list_date'),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'Places.views.home', name='home'),
#    # url(r'^Places/', include('Places.foo.urls')),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#)

#    
#- - list the places by: 1) descending date; 2) number of views
#- - view a place (viewing a place increments its number of views)
