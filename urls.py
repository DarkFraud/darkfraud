# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

# Auth
urlpatterns += patterns('',
    (r'^accounts/login/$',  'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/register/$', 'darkfraud.blog.views.register'),
    (r'^accounts/profile/$', 'darkfraud.blog.views.profile'),
)

# Blog
urlpatterns += patterns('',
    (r'^$', 'darkfraud.blog.views.home'),
    (r'^category/(?P<slug>[-\w]+)/$', 'darkfraud.blog.views.category'),
    (r'^tag/(?P<slug>[-\w]+)/$', 'darkfraud.blog.views.tag'),
    (r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'darkfraud.blog.views.post'),
    (r'^arhive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'darkfraud.blog.views.arhive'),
    (r'^search/$', 'darkfraud.blog.views.search'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )