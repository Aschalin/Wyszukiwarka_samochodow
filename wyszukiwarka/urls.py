from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wyszukiwanie/$', views.wyszukiwanie, name='wyszukiwanie'),
    url(r'^przegladanie/(?P<s_id>[\w\-]+)/$', views.przegladanie, name='przegladanie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', views.silnik, name='silnik'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)$', views.nadwozie, name='nadwozie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)$', views.model, name='model'),
    url(r'^porownanie/(?P<s_id>[\w\-]+)/$', views.porownanie, name='porownanie'),
]