from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (ShowListView, ShowCreateView, ShowUpdateView,
                    NewShowTemplateView, ShowDetailView, ShowSearchView, HostCreateView)

urlpatterns = [
    url(r'^$', ShowListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ShowDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', ShowUpdateView.as_view(), name='update'),
    url(r'^new/$', NewShowTemplateView.as_view(), name='new'),
    url(r'^create/$', ShowCreateView.as_view(), name='create'),
    url(r'^search/$', ShowSearchView.as_view(), name='search'),
    url(r'^hosts/create/$', HostCreateView.as_view(), name='host_create'),
]
