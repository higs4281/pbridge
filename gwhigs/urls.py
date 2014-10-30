from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from class_based_auth_views.views import LoginView, LogoutView

from .views import IndexView, AboutTemplateView
from .forms import LoginForm

import autocomplete_light

# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^navigation/', include('navigation_autocomplete.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutTemplateView.as_view(), name='about'),
    url(r'^login/', LoginView.as_view(form_class=LoginForm), name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
    url(r'^shows/', include('shows.urls', namespace='shows')),
    
]
