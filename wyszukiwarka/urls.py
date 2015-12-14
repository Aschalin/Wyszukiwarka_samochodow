from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wyszukiwanie$', views.wyszukiwanie, name='wyszukiwanie'),
    url(r'^przegladanie$', views.przegladanie, name='przegladanie'),
]