from __future__ import absolute_import
from __future__ import unicode_literals

import autocomplete_light

from .models import Client, Budget

# This will generate a ShowAutocomplete class
autocomplete_light.register(
    Client,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 0,
        'placeholder': 'Client search',
    },
)

# This will generate a ShowAutocomplete class
autocomplete_light.register(
    Budget,
    # Just like in ModelAdmin.search_fields
    search_fields=['name', 'client__name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 0,
        'placeholder': 'Budget search',
    },
    add_another_url_name='clients:budget_create'
)
