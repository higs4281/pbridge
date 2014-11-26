from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin


def close(request):
    """
    Closes the current page. Useful for popup forms. Use for success_url.
    """
    return HttpResponse(
        '<script type="text/javascript">'
        'window.close(); window.opener.parent.location.reload();'
        '</script>'
    )


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class DashboardView(LoginRequiredMixin, PermissionRequiredMixin,
                    RedirectView):
    """
    Handles traffic by directing users to the friendliest page it can
    find for them.
    """

    permission_required = 'is_authenticated'
    # Currently lazy, just redirecting to shows
    pattern_name = 'shows:index'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'