from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Ad
from .forms import AdCreateForm, AdUpdateForm


class AdActionMixin(object):
    """
    A mixin for gathering code that is common to both the create and
    update views for the Ad model
    """

    exclude = []

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(AdActionMixin, self).form_valid(form)


class AdCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                   AdActionMixin, CreateView):
    """
    Base view for creating an ad. Allows pre-filled data to
    be generated if both 'platform' and 'id' are passed in the URL.
    """

    model = Ad
    permission_required = 'is_staff'
    success_msg = 'Ad created'
    form_class = AdCreateForm


class AdUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                   AdActionMixin, UpdateView):
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