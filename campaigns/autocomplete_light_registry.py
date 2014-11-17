from __future__ import absolute_import, unicode_literals

import autocomplete_light

from .models import Campaign

# This will generate a CampaignAutocomplete class
autocomplete_light.register(
    Campaign,
    # Just like in ModelAdmin.search_fields
    search_fields=['name', 'client__name', 'budget__name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    attrs={
        'data-autocomplete-minimum-characters': 0,
        'placeholder': 'Campaign search',
    },
)
