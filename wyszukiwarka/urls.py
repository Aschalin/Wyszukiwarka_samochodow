from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wyszukiwanie/$', views.wyszukiwanie, name='wyszukiwanie'),
    url(r'^przegladanie/(?P<s_id>[\w\-]+)/$', views.przegladanie, name='przegladanie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', views.silnik, name='silnik'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)$', views.nadwozie, name='nadwozie'),
    url(r'^szczegoly/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)$', views.model, name='model'),
    url(r'^porownanie/(?P<s_id>[\w\-]+)/$', views.porownanie, name='porownanie'),
    url(r'^login/$', login, name='login'),
    url(r'^moderate/$', views.moderate, name='moderate'),
    url(r'^editSilnik/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', views.editSilnik, name='editSilnik'),
    url(r'^editNadwozie/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)$', views.editNadwozie, name='editNadwozie'),
    url(r'^editSamochod/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)$', views.editSamochod, name='editSamochod'),
    url(r'^editParametry/(?P<s_id>[\w\-]+)/(?P<c_id>[\w\-]+)/(?P<n_id>[\w\-]+)/(?P<e_id>[\w\-]+)$', views.editParametry, name='editParametry'),
    url(r'^logout/$',views.logout_page, name='logout'),
]