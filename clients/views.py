from __future__ import absolute_import, unicode_literals
import autocomplete_light

from django.views.generic import DetailView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Client, Budget
from .forms import BudgetCreateForm


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
                       autocomplete_light.CreateView):
    """
    Quick Budget creation.
    """

    model = Budget
    form_class = BudgetCreateForm
    permission_required = 'is_staff'