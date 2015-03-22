from __future__ import unicode_literals, absolute_import

import django_filters

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
            'hosts__first_name': ['icontains'],
            'hosts__last_name': ['icontains'],
            'platform': ['exact'],
            'tags': ['icontains'],
            'default_vendor': ['exact'],
            'api_id': ['exact'],
            'notes': ['icontains'],
        }
        form = ShowSearchForm