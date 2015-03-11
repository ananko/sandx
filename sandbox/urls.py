from django.conf.urls import patterns, url
from sandbox import views

urlpatterns = patterns('',
        url(r'^$', views.overview, name='overview'),
        url(r'^profile$', views.profile, name='profile'),
)

