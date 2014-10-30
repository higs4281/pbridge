from __future__ import unicode_literals, absolute_import

import floppyforms as forms
import django_filters
from crispy_forms.helper import FormHelper

from .models import Show
from .forms import ShowSearchForm


class ShowSearchFilter(django_filters.FilterSet):
    """
    FilterSet for searching Shows.
    Crispy form handling is done in ShowSearchForm.
    """

    class Meta:
        model = Show
        fields = {
            'name': ['icontains'],
            'host__name': ['icontains'],
            'platform': ['exact'],
            'tags': ['icontains'],
            'default_vendor': ['exact'],
            'api_id': ['exact'],
            'notes': ['icontains'],
        }
        form = ShowSearchForm