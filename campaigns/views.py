from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import UpdateWithInlinesView

import shows.mixins as mixins
from .models import Campaign
from . import forms


class CampaignListView(LoginRequiredMixin, PermissionRequiredMixin,
                       mixins.PrefetchRelatedMixin, ListView):
    """
    Base view for a list of campaigns.
    """

    model = Campaign
    permission_required = 'is_staff'
    prefetch_related = ['client', 'budget']


class CampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                         mixins.SuccessMessageMixin, CreateView):
    """

    """

    model = Campaign
    form_class = forms.CampaignCreateForm
    template_name = 'campaigns/campaign_create.html'
    success_msg = 'Campaign created'
    permission_required = 'is_staff'


class CampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                         mixins.SelectRelatedMixin, DetailView):
    """
    Base view for looking at a Campaign
    """

    model = Campaign
    permission_required = 'is_staff'
    select_related = 'ad'

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data()
        ad_list = self.object.ad_set.all().order_by('vendor__name', 'show__name')
        context['ad_list'] = ad_list
        return context


class CampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                         mixins.SuccessMessageMixin, mixins.SelectRelatedMixin,
                         UpdateWithInlinesView):
    """
    Update view for Campaigns. Includes Ads inline.
    """

    model = Campaign
    permission_required = 'is_staff'
    select_related = 'client'
    form_class = forms.CampaignUpdateForm
    success_msg = 'Campaign updated'
    inlines = [forms.AdsInline]

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdateView, self).get_context_data(**kwargs)
        helper = forms.AdsInlineFormHelper()
        context['inlines_helper'] = helper
        return context