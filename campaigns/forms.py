from __future__ import absolute_import, unicode_literals

import autocomplete_light
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton

from .models import Campaign


class CampaignAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Campaign
        exclude = []


class CampaignCreateForm(forms.ModelForm):
    """

    """

    def __init__(self, *args, **kwargs):
        super(CampaignCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        btn = StrictButton('Save', type='submit', css_class='btn btn-default')
        self.helper.add_input(btn)

    class Meta:
        model = Campaign
        fields = [
            'name',
            'client',
            'budget',
        ]