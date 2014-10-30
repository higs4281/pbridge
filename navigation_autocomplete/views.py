from __future__ import absolute_import
from __future__ import unicode_literals

from django import shortcuts
from django.db.models import Q
from django.contrib.auth.models import User, Group

from shows.models import Client, Show, Vendor


def navigation_autocomplete(request,
    template_name='navigation_autocomplete/autocomplete.html'):

    q = request.GET.get('q', '')
    context = {'q': q}

    queries = {}
    queries['users'] = User.objects.filter(
        Q(username__icontains=q) |
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(email__icontains=q)
    ).distinct()[:3]
    queries['groups'] = Group.objects.filter(name__icontains=q)[:3]
    queries['shows'] = Show.objects.filter(
        Q(name__icontains=q) |
        Q(host__icontains=q)
    ).distinct()[:3]
    queries['clients'] = Client.objects.filter(name__icontains=q)[:3]
    queries['vendors'] = Vendor.objects.filter(name__icontains=q)[:3]

    context.update(queries)

    return shortcuts.render(request, template_name, context)
