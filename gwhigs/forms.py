from django.contrib.auth.forms import AuthenticationForm

import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_forms.bootstrap import StrictButton


class LoginForm(AuthenticationForm, forms.Form):
    """
    Base login form, built from the django built-in auth system.
    """

    # Override form fields
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Field('username', placeholder='username'),
                Field('password', placeholder='password'),
                StrictButton(
                    'Sign in',
                    type='submit',
                    css_class='btn btn-default'
                ),
                css_class='col-sm-6 col-md-4 col-md-offset-4',
            ),
        )
