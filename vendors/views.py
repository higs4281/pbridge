from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

import autocomplete_light

from . import models
from . import forms


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                      autocomplete_light.CreateView):
    """
    Popup Order creation.
    """

    model = models.Order
    permission_required = 'is_staff'
    form_class = forms.OrderCreateForm