from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import UpdateWithInlinesView

from shows.mixins import SelectRelatedMixin, PrefetchRelatedMixin
from .models import Campaign
from .forms import CampaignCreateForm, AdsInline, AdsInlineFormHelper, CampaignUpdateForm


class CampaignListView(LoginRequiredMixin, PermissionRequiredMixin,
                       PrefetchRelatedMixin, ListView):
    """
    Base view for a list of campaigns.
    """

    model = Campaign
    permission_required = 'is_staff'
    prefetch_related = ['client', 'budget']


class CampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                         CreateView):
    """

    """

    model = Campaign
    form_class = CampaignCreateForm
    permission_required = 'is_staff'


class CampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                         SelectRelatedMixin, DetailView):
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
                         SelectRelatedMixin, UpdateWithInlinesView):
    """
    Update view for Campaigns. Includes Ads inline.
    """

    model = Campaign
    permission_required = 'is_staff'
    select_related = 'client'
    form_class = CampaignUpdateForm
    inlines = [AdsInline]

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdateView, self).get_context_data(**kwargs)
        helper = AdsInlineFormHelper()
        context['inlines_helper'] = helper
        return context
