from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.http import HttpResponse
import django.views.generic as generic

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django_filters.views import FilterView
import autocomplete_light
from rest_framework import generics

from .admin import ShowResource
from .models import Show, Host, Platform
from .forms import ShowCreateForm, ShowUpdateForm, HostCreateForm
from .filters import ShowSearchFilter
from .mixins import SuccessMessageMixin, PrefetchRelatedMixin, SelectRelatedMixin
from .serializers import ShowSerializer


class HostCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     autocomplete_light.CreateView):
    """
    Popup Host creation
    """
    model = Host
    form_class = HostCreateForm
    permission_required = 'is_staff'


class HostUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, generic.UpdateView):
    """
    Popup Host creation
    """
    model = Host
    form_class = HostCreateForm
    permission_required = 'is_staff'
    success_msg = 'Host Updated'


class HostDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.DetailView):
    model = Host
    permission_required = 'is_staff'


class NewShowTemplateView(generic.TemplateView):
    template_name = 'shows/new_show.html'


class ShowCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, generic.CreateView):
    """
    Base view for creating a show. Allows pre-filled data to
    be generated if both 'platform' and 'id' are passed in the URL.
    """

    model = Show
    form_class = ShowCreateForm
    permission_required = 'is_staff'
    success_msg = 'Show created'

    def get_initial(self):
        initial = super(ShowCreateView, self).get_initial()
        platform = self.request.GET.get('platform')
        _id = self.request.GET.get('id')
        try:
            platform_id = int(platform)
        except ValueError:
            return initial
        platform_class = Platform.CLASS_DICT.get(platform_id)
        if platform_class and _id:
            api = platform_class(show_api_id=_id)
            initial.update(api.get_show_initial())
            initial['platform'] = Platform.objects.get(id=platform_id)
        return initial


class ShowUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, generic.UpdateView):
    model = Show
    permission_required = 'is_staff'
    success_msg = 'Show updated'
    form_class = ShowUpdateForm


class ShowListView(LoginRequiredMixin, PermissionRequiredMixin,
                   PrefetchRelatedMixin, generic.ListView):
    model = Show
    permission_required = 'is_staff'
    prefetch_related = ['platform', 'default_vendor', 'hosts']

    def get_queryset(self):
        # FROM 2 SCOOPS 1.6
        # Fetch the queryset from the parent get_queryset
        queryset = super(ShowListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")
        if q:
            # Return a filtered queryset
            return queryset.filter(
                Q(name__icontains=q) |
                Q(host__icontains=q) |
                Q(default_vendor__icontains=q)
            )
        # Return the base queryset
        return queryset


class ShowDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                     SelectRelatedMixin, generic.DetailView):
    """
    Base view for looking at a single Show object.
    """
    model = Show
    permission_required = 'is_staff'
    select_related = 'ad'


class ShowSearchView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    """
    Base Search page for shows.
    """
    permission_required = 'is_staff'
    template_name = 'shows/show_search.html'
    filterset_class = ShowSearchFilter


class ShowExportView(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.View):
    """
    Base view for exporting Shows as csv files.
    See also:
    http://stackoverflow.com/questions/24008820/use-django-import-export-with-class-based-views
    """
    permission_required = 'is_staff'

    def get(self, *args, **kwargs):
        dataset = ShowResource().export()
        response = HttpResponse(dataset.csv, content_type='csv')
        response['Content-Disposition'] = 'attachment; filename=shows.csv'
        return response


class ShowAPIListView(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    filter_fields = (
        'name',
        'platform',
        'notes',
        'active',
        'default_vendor',
    )


class ShowAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer