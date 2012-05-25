from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^blog/$', 'blog.views.index'),
    (r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'blog.views.detail'),
    (r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$', 'blog.views.month'),
    (r'^blog/(?P<year>\d{4})/$', 'blog.views.year'),

    (r'^$', direct_to_template, {'template': 'index.html'}),

    (r'^contact/', include('contact_form.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

if settings.LOCAL_MEDIA:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT + "/",
            'show_indexes': True
        }),
    )
