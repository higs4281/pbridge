from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import navigation_autocomplete

urlpatterns = patterns('',
    url(r'^$', navigation_autocomplete, name='navigation_autocomplete'),
)
