from __future__ import absolute_import, unicode_literals

import autocomplete_light
# Use floppyforms.__future__ for seamless modelform functionality (until 1.3)
import floppyforms.__future__ as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Vendor, Order


class OrderAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Order
        exclude = []