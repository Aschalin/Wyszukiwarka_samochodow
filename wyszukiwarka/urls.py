from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wyszukiwanie/$', views.wyszukiwanie, name='wyszukiwanie'),
    url(r'^przegladanie/(?P<s_id>[\w\-]+)/$', views.przegladanie, name='przegladanie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/$', views.szczegoly, name='szczegoly'),
    url(r'^porownanie/(?P<s_id>[\w\-]+)/$', views.porownanie, name='porownanie'),
]