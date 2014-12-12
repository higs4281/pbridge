from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.http import HttpResponse
import django.views.generic as generic

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django_filters.views import FilterView
import autocomplete_light
from rest_framework import generics

from .admin import ShowResource
from .models import Show, Host
from .forms import ShowCreateForm, ShowUpdateForm, HostCreateForm
from .filters import ShowSearchFilter
from .mixins import SuccessMessageMixin, PrefetchRelatedMixin
from .serializers import ShowSerializer
from .utils import yt_init_data, it_init_data


class NewShowTemplateView(generic.TemplateView):
    template_name = 'shows/new_show.html'


class ShowCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, generic.CreateView):
    """
    Base view for creating a show. Allows pre-filled data to
    be generated if both 'platform' and 'id' are passed in the URL.
    """

    model = Show
    permission_required = 'is_staff'
    success_msg = 'Show created'
    form_class = ShowCreateForm

    def get_initial(self):
        initial = super(ShowCreateView, self).get_initial()
        platform = self.request.GET.get('platform')
        _id = self.request.GET.get('id')

        if platform and _id:
            if platform == 'yt':
                initial.update(yt_init_data(_id))
            elif platform == 'it':
                initial.update(it_init_data(_id))

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
    prefetch_related = ['platform', 'host', 'default_vendor']

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
                     generic.DetailView):
    """
    Base view for looking at a single Show object.
    """

    model = Show
    permission_required = 'is_staff'


class ShowSearchView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    """
    Base Search page for shows.
    """

    permission_required = 'is_staff'
    template_name = 'shows/show_search.html'
    filterset_class = ShowSearchFilter


class HostCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     autocomplete_light.CreateView):
    """
    Popup Host creation
    """
    model = Host
    form_class = HostCreateForm
    permission_required = 'is_staff'


class HostDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.DetailView):
    model = Host
    permission_required = 'is_staff'


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


class ShowAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer