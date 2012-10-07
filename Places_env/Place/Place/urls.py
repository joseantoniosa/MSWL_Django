from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Place_app.views',
    url(r'^$', 'view'),
    url(r'^place/(?P<r_id>d+)/$', 'list_date'),
    ## url(r'^place/(?P<r_id>d+)/$', 'list_date'),
    url(r'^create/$', 'create'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^view/post/(?P<p_id>d+)/$','view', name = 'list_date'),
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
