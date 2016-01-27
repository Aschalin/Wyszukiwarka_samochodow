from django.conf.urls import url
from django.contrib.auth.views import login

from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^wyszukiwanie/$', wyszukiwanie, name='wyszukiwanie'),
    url(r'^przegladanie/(?P<s_id>[\w\-]+)/$', przegladanie, name='przegladanie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', silnik, name='silnik'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)$', nadwozie, name='nadwozie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)$', model, name='model'),
    url(r'^porownanie/(?P<s_id>[\w\-]+)/$', porownanie, name='porownanie'),
    url(r'^login/$', login, name='login'),
    url(r'^moderate/$', moderate, name='moderate'),
    url(r'^editSilnik/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', editSilnik, name='editSilnik'),
    url(r'^editNadwozie/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)$', editNadwozie, name='editNadwozie'),
    url(r'^editSamochod/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)$', editSamochod, name='editSamochod'),
    url(r'^editParametry/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', editParametry, name='editParametry'),
    url(r'^logout/$', logout_page, name='logout'),
]
