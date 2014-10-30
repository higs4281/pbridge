from __future__ import absolute_import, unicode_literals

import autocomplete_light
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Ad


class AdAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Ad
        exclude = []


class AdForm(forms.ModelForm):
    """
    Base form for the Ad model. Adds crispy_forms functionality in the
    __init__ function with the FormHelper class.
    """

    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can then dynamically adjust your layout
        self.helper.add_input(Submit('save', 'Save'))


class AdCreateForm(AdForm):
    """
    For Show creation. Inherits from AdForm.
    """

    class Meta:
        model = Ad
        fields = [
            'campaign',
            'vendor',
            'cost',
            'cost_type',
            'instructions',
        ]


class AdUpdateForm(AdForm):
    """
    For updating Ads. Inherits from AdForm.
    """

    class Meta:
        model = Ad
        exclude = []