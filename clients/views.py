from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ImproperlyConfigured

from django.views.generic import DetailView, ListView, CreateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import InlineFormSet, UpdateWithInlinesView
from ads.models import Ad

from .models import Client, Budget, Campaign
from .forms import BudgetCreateForm, CampaignCreateForm


class PrefetchRelatedMixin(object):
    """
    Allows a CBV to use prefetch_related on their queryset.
    """
    prefetch_related = None

    def get_queryset(self):
        if self.prefetch_related is None:
            msg = ('{} is missing the prefetch_related property. This must '
                   'be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        if not isinstance(self.prefetch_related, (tuple, list)):
            msg = ("{}'s prefetch_related property "
                   'must be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        queryset = super(PrefetchRelatedMixin, self).get_queryset()
        return queryset.prefetch_related(*self.prefetch_related)


class SelectRelatedMixin(object):
    """
    Allows a CBV to use select_related on their queryset.
    """
    select_related = None

    def get_queryset(self):
        if self.select_related is None:
            msg = ('{} is missing the select_related property. This must '
                   'be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        queryset = super(SelectRelatedMixin, self).get_queryset()

        return queryset.select_related(self.select_related)


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                       DetailView):
    """
    Simple view for details on a client.
    """

    model = Client
    permission_required = 'is_staff'


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin,
                     ListView):
    """

    """

    model = Client
    permission_required = 'is_staff'


class BudgetCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                       CreateView):
    """
    Quick Budget creation.
    """

    model = Budget
    form_class = BudgetCreateForm
    permission_required = 'is_staff'


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


class AdsInline(InlineFormSet):
    model = Ad


class CampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                         SelectRelatedMixin, UpdateWithInlinesView):
    """
    Update view for Campaigns. Includes Ads inline.
    """

    model = Campaign
    form_class = CampaignCreateForm
    inlines = [AdsInline]