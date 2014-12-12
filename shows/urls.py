from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShowListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ShowDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ShowUpdateView.as_view(), name='update'),
    url(r'^new/$', views.NewShowTemplateView.as_view(), name='new'),
    url(r'^create/$', views.ShowCreateView.as_view(), name='create'),
    url(r'^search/$', views.ShowSearchView.as_view(), name='search'),
    url(r'^export/$', views.ShowExportView.as_view(), name='export'),
    url(r'^hosts/create/$', views.HostCreateView.as_view(), name='host_create'),
    url(r'^hosts/(?P<pk>\d+)/$', views.HostDetailView.as_view(), name='host_detail'),
    # API URL's
    url(r'^api/$', views.ShowAPIListView.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.ShowAPIDetailView.as_view()),
]
