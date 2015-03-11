from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda r: HttpResponseRedirect('sandbox/')),
    url(r'^sandbox/', include('sandbox.urls', namespace='sandbox')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
