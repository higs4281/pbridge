from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import AdListView, AdUpdateView, AdDetailView

urlpatterns = [
    url(r'^$', AdListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', AdDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', AdUpdateView.as_view(), name='update'),
]
