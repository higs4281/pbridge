from __future__ import absolute_import, unicode_literals

import autocomplete_light
from django.core.exceptions import ValidationError
import floppyforms.__future__ as forms  # Use __future__ until 1.3
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import StrictButton

from .models import Show, Host

autocomplete_light.autodiscover()


class ShowAdminForm(autocomplete_light.ModelForm):
    """
    Adds autocomplete_light functionality to admin forms for the Django Admin site.
    """

    class Meta:
        model = Show
        exclude = []


class ShowForm(autocomplete_light.ModelForm):
    """
    Base form for the Show model. Adds crispy_forms functionality in the
    __init__ function with the FormHelper class.
    """

    def __init__(self, *args, **kwargs):
        super(ShowForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('save', 'Save'))


class ShowCreateForm(autocomplete_light.ModelForm):
    """
    For Show creation.
    """

    def __init__(self, *args, **kwargs):
        super(ShowCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    'api_id',
                    'link',
                    'feed',
                    'description',
                    css_class='col-sm-6'
                ),
                Div(
                    'default_vendor',
                    'platform',
                    'art',
                    'tags',
                    'notes',
                    css_class='col-sm-6'
                ),
                css_class='row'
            ),
        )
        self.helper.add_input(Submit('save', 'Save'))

    def clean_api_id(self):
        # Shouldn't create duplicate api_id's
        # (making api_id 'unique-ish')
        data = self.cleaned_data.get('api_id')
        if data:
            api_id_exists = Show.objects.filter(api_id=data)
            if api_id_exists:
                msg = 'A show already exists with that API ID.'
                raise ValidationError(msg)
        return data

    class Meta:
        model = Show
        fields = [
            'default_vendor',
            'name',
            'api_id',
            'feed',
            'platform',
            'tags',
            'description',
            'link',
            'notes',
        ]


class ShowUpdateForm(ShowForm):
    """
    For updating Shows. Inherits from ShowForm.
    """

    def __init__(self, *args, **kwargs):
        super(ShowUpdateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    'host',
                    'api_id',
                    'link',
                    'description',
                    css_class='col-md-5'
                ),
                Div(
                    'tags',
                    'feed',
                    'art',
                    'notes',
                    css_class='col-md-5'
                ),
                Div(
                    'platform',
                    'default_vendor',
                    'downloads_per_episode',
                    'episodes_per_month',
                    'active',
                    css_class='col-md-2'
                ),
                css_class='row'
            ),
        )
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Show
        fields = [
            'name',
            'host',
            'api_id',
            'platform',
            'tags',
            'art',
            'description',
            'link',
            'feed',
            'episodes_per_month',
            'downloads_per_episode',
            'default_vendor',
            'active',
            'notes',
        ]


class ShowSearchForm(forms.Form):
    """
    Base form for the Show Search page. Both Crispy and Floppy.
    """

    # Crispy form for the ShowSearchFilterSet
    def __init__(self, *args, **kwargs):
        super(ShowSearchForm, self).__init__(*args, **kwargs)
        self.fields['default_vendor'].label = 'Vendor'
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Div(
                    'name__icontains',
                    'host__name__icontains',
                    'default_vendor',
                    css_class='col-sm-6'
                ),
                Div(
                    'platform',
                    'api_id',
                    'notes__icontains',
                    css_class='col-sm-6'
                ),
                css_class='row'
            ),
            StrictButton('Search', type='submit', css_class='btn-default')
        )


class HostCreateForm(forms.ModelForm):
    """
    Quick Host creation form.
    """

    def __init__(self, *args, **kwargs):
        super(HostCreateForm, self).__init__(*args, **kwargs)

        # Custom Crispiness
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = Host
        fields = [
            'name',
        ]