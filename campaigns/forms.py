from __future__ import absolute_import, unicode_literals

import autocomplete_light
from crispy_forms.layout import HTML, Submit, Div
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper, Layout
from extra_views import InlineFormSet

from ads.models import Ad
from .models import Campaign

autocomplete_light.autodiscover()

BUDGET_PLUS = HTML(
    """<a href="{% url 'clients:budget_create' %}" target="_blank">"""
    '<i id="plus" class="glyphicon glyphicon-plus"></i>'
    '</a>'
)


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
            BUDGET_PLUS,
        )
        self.helper.add_input(Submit("submit", "Save"))

    class Meta:
        model = Campaign
        fields = [
            'name',
            'client',
            'budget',
        ]


class CampaignUpdateForm(autocomplete_light.ModelForm):
    """

    """
    def __init__(self, *args, **kwargs):
        super(CampaignUpdateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        # Since we have 2 forms to render, handle the <form> tag in template
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    css_class='col-md-4'
                ),
                Div(
                    'client',
                    css_class='col-md-4'
                ),
                Div(
                    'budget',
                    BUDGET_PLUS,
                    css_class='col-md-4'
                ),
                css_class='row'
            ),
        )

    class Meta:
        model = Campaign
        fields = [
            'name',
            'client',
            'budget',
        ]


class AdsInline(InlineFormSet):
    model = Ad
    fields = [
        'campaign',
        'show',
        'scheduled_date',
        'vendor',
        'cost',
        'cost_type',
    ]


class AdsInlineFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AdsInlineFormHelper, self).__init__(*args, **kwargs)
        self.template = 'bootstrap/table_inline_formset.html'
        # Since we have 2 forms to render, handle the <form> tag in template
        self.form_tag = False