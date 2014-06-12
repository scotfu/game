#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
#admin.autodiscover()


import xadmin
xadmin.autodiscover()

# version Model
#from xadmin.plugins import xversion
#xversion.registe_models()

urlpatterns = patterns('',
                           url(r'admin/', include(xadmin.site.urls)),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'game.views.home', name='home'),
    # url(r'^game/', include('game.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
     url(r'^', include('records.urls')),
     url(r'^$', 'records.views.render_game'),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, },
        name='static'),
                    )

