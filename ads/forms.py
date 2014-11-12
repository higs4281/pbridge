from __future__ import absolute_import, unicode_literals

import autocomplete_light
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

from .models import Ad

autocomplete_light.autodiscover()

class AdAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Ad
        exclude = []


class AdCreateForm(forms.ModelForm):
    """
    For quick Ad creation.
    """

    def __init__(self, *args, **kwargs):
        super(AdCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Ad
        fields = [
            'campaign',
            'vendor',
            'cost',
            'cost_type',
            'instructions',
        ]


class AdUpdateForm(forms.ModelForm):
    """
    For updating Ads.
    """

    def __init__(self, *args, **kwargs):
        super(AdUpdateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    'show',
                    'campaign',
                    'vendor',
                    'instructions',
                    css_class='col-md-5'
                ),
                Div(
                    'scheduled_date',
                    'cost',
                    'projected_views',
                    'order',
                    'episode',
                    'timestamp',
                    css_class='col-md-5'
                ),
                Div(
                    'views_guaranteed',
                    'cost_type',
                    'verified',
                    'makegood_needed',
                    'notes',
                    css_class='col-md-2'
                ),
                css_class='row'
            )
        )
        # self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Ad
        fields = [
            'campaign',
            'show',
            'vendor',
            'scheduled_date',
            'cost',
            'projected_views',
            'views_guaranteed',
            'cost_type',
            'order',
            'instructions',
            'episode',
            'timestamp',
            'verified',
            'notes',
            'makegood_needed'
        ]