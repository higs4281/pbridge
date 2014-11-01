from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (CampaignListView, CampaignCreateView, CampaignDetailView,
                    CampaignUpdateView)

urlpatterns = [
    url(r'^$', CampaignListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', CampaignDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', CampaignUpdateView.as_view(), name='update'),
    url(r'^create/$', CampaignCreateView.as_view(), name='create'),
]
