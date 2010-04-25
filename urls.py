from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^discusser/', include('discusser.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'fbdiscuss.views.index', name='fbdiscuss.index'),
    url(r'^create/$', 'fbdiscuss.views.create', name='fbdiscuss.create'),
    url(r'^discuss/(?P<guid>[-\w]+)/$', 'fbdiscuss.views.discuss', name='fbdiscuss.discuss'),
    url(r'^list/$', 'fbdiscuss.views.list', name='fbdiscuss.list'),
)
