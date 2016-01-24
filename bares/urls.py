from django.conf.urls import patterns, url
from bares import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bar/(?P<id>[0-9]+)/$', views.bar, name='bar'),
        url(r'^registro/$', views.registro, name='registro'),
        url(r'^logout/$', views.salir, name='logout'),
)
