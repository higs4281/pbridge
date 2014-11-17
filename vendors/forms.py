from __future__ import absolute_import, unicode_literals

import autocomplete_light
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Order


class OrderAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Order
        exclude = []


class OrderCreateForm(autocomplete_light.ModelForm):
    """
    Popup Order creation form
    """

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Order
        fields = [
            'name',
            'vendor',
            'client',
        ]