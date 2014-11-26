from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import UpdateWithInlinesView

import shows.mixins as mixins
from . import models
from . import forms

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LogInitialValueMixin(object):
    def get_form(self, form_class):
        form = super(LogInitialValueMixin, self).get_form(form_class)
        logger.debug(form.initial)
        return form


class CampaignListView(LoginRequiredMixin, PermissionRequiredMixin,
                       mixins.PrefetchRelatedMixin, ListView):
    """
    Base view for a list of campaigns.
    """

    model = models.Campaign
    permission_required = 'is_staff'
    prefetch_related = ['client', 'budget']


class CampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                         mixins.SuccessMessageMixin, CreateView):
    """

    """

    model = models.Campaign
    form_class = forms.CampaignCreateForm
    template_name = 'campaigns/campaign_create.html'
    success_msg = 'Campaign created'
    permission_required = 'is_staff'


class CampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                         DetailView):
    """
    Base view for looking at a Campaign
    """

    model = models.Campaign
    permission_required = 'is_staff'

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data()
        ad_list = self.object.ad_set.all().prefetch_related(
            'vendor', 'show', 'show__platform'
        ).order_by('vendor__name', 'show__name')
        context['ad_list'] = ad_list
        return context


class CampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                         mixins.SuccessMessageMixin, UpdateWithInlinesView):
    """
    Update view for Campaigns. Includes Ads inline.
    """

    model = models.Campaign
    permission_required = 'is_staff'
    form_class = forms.CampaignUpdateForm
    success_msg = 'Campaign updated'
    inlines = [forms.AdsInline]

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdateView, self).get_context_data(**kwargs)
        helper = forms.AdsInlineFormHelper()
        context['inlines_helper'] = helper
        return context