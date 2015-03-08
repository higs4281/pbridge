from __future__ import absolute_import, unicode_literals
from django.utils import timezone

from django.views.generic import UpdateView, ListView, DetailView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Ad
from .forms import AdUpdateForm
from shows.mixins import SuccessMessageMixin, SelectRelatedMixin, PrefetchRelatedMixin


class AdUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                   SuccessMessageMixin, UpdateView):
    model = Ad
    permission_required = 'is_staff'
    success_msg = 'Show updated'
    form_class = AdUpdateForm


class AdListView(LoginRequiredMixin, PermissionRequiredMixin,
                 PrefetchRelatedMixin, ListView):
    model = Ad
    prefetch_related = ['campaign', 'campaign__client', 'show']
    permission_required = 'is_staff'

    def get_queryset(self):
        queryset = super(AdListView, self).get_queryset()

        # Filter and order
        return queryset.filter(
            scheduled_date__lte=timezone.now().date()
        ).order_by('-verified', '-scheduled_date')


class AdDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                   SelectRelatedMixin, DetailView):
    model = Ad
    permission_required = 'is_staff'
    select_related = 'episode'

    def get_context_data(self, **kwargs):
        """
        Add a list of recent episodes to the view's context
        for selection on the page, if the episode isn't created yet.
        """
        context = super(AdDetailView, self).get_context_data(**kwargs)
        if not self.object.episode:
            show = self.object.show
            platform_class = show.platform.get_api_class()
            api = platform_class(show_api_id=show.api_id)
            episode_list = api.get_episode_list()
            context['episode_list'] = episode_list
            context['platform'] = show.platform.simple_name
        return context


class AdUnverifiedView(LoginRequiredMixin, PermissionRequiredMixin,
                       ListView):
    model = Ad
    permission_required = 'is_staff'

    def get_queryset(self):
        qs = super(AdUnverifiedView, self).get_queryset()
        return qs.filter(verified=False)
