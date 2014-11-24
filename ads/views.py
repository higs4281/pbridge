from __future__ import absolute_import, unicode_literals
from django.utils import timezone

from django.views.generic import UpdateView, ListView, DetailView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Ad
from .forms import AdUpdateForm
from shows.mixins import SuccessMessageMixin, SelectRelatedMixin


class AdUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                   SuccessMessageMixin, UpdateView):
    model = Ad
    permission_required = 'is_staff'
    success_msg = 'Show updated'
    form_class = AdUpdateForm


class AdListView(LoginRequiredMixin, PermissionRequiredMixin,
                 ListView):
    model = Ad
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


class AdUnverifiedView(LoginRequiredMixin, PermissionRequiredMixin,
                       ListView):
    model = Ad
    permission_required = 'is_staff'

    def get_queryset(self):
        qs = super(AdUnverifiedView, self).get_queryset()
        return qs.filter()
