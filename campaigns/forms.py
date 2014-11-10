from __future__ import absolute_import, unicode_literals

import autocomplete_light
from crispy_forms.layout import HTML
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper, Layout
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
        self.helper.layout = Layout(
            'name',
            'client',
            'budget',
            HTML(
                '<a href="/clients/budgets/create/" target="_blank">'
                '<i id="big-glyph" class="glyphicon glyphicon-plus"></i>'
                '</a><br>'
            ),
            StrictButton('Save', type='submit', css_class='btn btn-default')
        )

    class Meta:
        model = Campaign
        fields = [
            'name',
            'client',
            'budget',
        ]