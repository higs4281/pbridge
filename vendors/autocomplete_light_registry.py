from __future__ import absolute_import
from __future__ import unicode_literals

import autocomplete_light

from .models import Vendor

# This will generate and register a ShowAutocomplete class
autocomplete_light.register(
    Vendor,
    # Just like in ModelAdmin.search_fields
    search_fields=['name', 'contact_name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to search.',
    },
)