from __future__ import absolute_import, unicode_literals

import autocomplete_light
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton

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

        # Custom Crispyness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        btn = StrictButton('Save', type='submit', css_class='btn btn-default')
        self.helper.add_input(btn)

    class Meta:
        model = Budget
        fields = [
            'name',
            'client',
            'amount',
        ]