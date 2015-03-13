from django.conf.urls import patterns, url
from sandbox import views

urlpatterns = patterns('',
        url(r'^$', views.overview, name='overview'),
        url(r'^profile$', views.profile, name='profile'),
        url(r'^notes$', views.notes, name='notes'),
        url(r'^notes/(?P<pk>\d+)/delete$', views.delete_note, name='delete_note'),
)

