from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from class_based_auth_views.views import LoginView, LogoutView

from .views import IndexView, AboutTemplateView, DashboardView
from .forms import LoginForm

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^navigation/', include('navigation_autocomplete.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutTemplateView.as_view(), name='about'),
    url(r'^login/', LoginView.as_view(form_class=LoginForm), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^close/', 'pbridge.views.close', name='close'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^shows/', include('shows.urls', namespace='shows')),
    url(r'^campaigns/', include('campaigns.urls', namespace='campaigns')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^ads/', include('ads.urls', namespace='ads')),
    
]
