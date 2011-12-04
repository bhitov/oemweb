from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('oemweb.server.views',
    url(r'^posts/$', 'post_list', name='post_list'),
    url(r'^posts/create/$', 'post_form', name='post_form'),
    url(r'^posts/createa/$', 'post_create_ajax', name='post_create_ajax'),
    url(r'^epipost/$', 'ep_post', name='ep_post'),
    url(r'^KML/create/$', 'KML_form', name='KML_form'),
    url(r'^KML/$', 'KML_form', name='KML_form'),
    url(r'^KML/(?P<title>\w+)/$', 'KML_detail', name='KML_detail')
    # Examples:
    # url(r'^$', 'oemweb.views.home', name='home'),
    # url(r'^oemweb/', include('oemweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
