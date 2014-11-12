from __future__ import absolute_import, unicode_literals

import autocomplete_light

from .models import Ad


autocomplete_light.register(
    Ad,
    search_fields=['client__name', 'episode__show', 'episode__date'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Client, Show or Date',
    },
)
