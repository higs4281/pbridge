from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse

from django.views.generic import DetailView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy

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
                       CreateView):
    """
    Quick Budget creation.
    """

    model = Budget
    form_class = BudgetCreateForm
    permission_required = 'is_staff'
    success_url = reverse_lazy('close')