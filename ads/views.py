from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.views.generic import UpdateView, ListView, DetailView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Ad
from .forms import AdUpdateForm
from shows.mixins import SuccessMessageMixin


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
        # FROM 2 SCOOPS 1.6
        # Fetch the queryset from the parent get_queryset
        queryset = super(AdListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")
        if q:
            # Return a filtered queryset
            return queryset.filter(
                Q(client__name__icontains=q) |
                Q(host__icontains=q) |
                Q(default_vendor__icontains=q)
            )
        # Retun the base queryset
        return queryset


class AdDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                   DetailView):
    model = Ad
    permission_required = 'is_staff'