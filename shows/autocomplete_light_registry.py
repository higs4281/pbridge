from __future__ import absolute_import
from __future__ import unicode_literals

import autocomplete_light
from taggit.models import Tag

from .models import Show, Host

# Taggit integration
autocomplete_light.register(
    Tag,
    attrs={
        'placeholder': 'Start typing to search.'
    }
)
# This will generate a ShowAutocomplete class
autocomplete_light.register(
    Show,
    # Just like in ModelAdmin.search_fields
    search_fields=['name', 'host', 'default_vendor'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to search.',
    },
)

autocomplete_light.register(
    Host,
    search_fields=['name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to search.',
    },
)
