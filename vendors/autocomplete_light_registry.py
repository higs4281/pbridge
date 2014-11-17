from __future__ import absolute_import, unicode_literals

import autocomplete_light

from . import models

# This will generate and register a ShowAutocomplete class
autocomplete_light.register(
    models.Vendor,
    # Just like in ModelAdmin.search_fields
    search_fields=['name', 'contact_name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to search.',
    },
)

autocomplete_light.register(
    models.Order,
    search_fields=['name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to search.',
    },
    add_another_url_name='vendors:order_create',
)