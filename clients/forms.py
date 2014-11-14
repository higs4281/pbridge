from __future__ import absolute_import, unicode_literals

import autocomplete_light
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Client, Budget


class ClientAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Client
        exclude = []


class BudgetAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Budget
        exclude = []


class BudgetCreateForm(forms.ModelForm):
    """
    Quick Budget creation form.
    """

    def __init__(self, *args, **kwargs):
        super(BudgetCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Budget
        fields = [
            'name',
            'client',
            'amount',
        ]