from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView, RedirectView

class IndexView(RedirectView):
    pattern_name = 'shows:index'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class Dashboard(RedirectView):
    """ Handles traffic by directing users to the friendliest page it can
        find for them.
    """
    pass