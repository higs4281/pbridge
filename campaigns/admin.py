from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Campaign
from .forms import CampaignAdminForm


@admin.register(Campaign)
class CampaignAdmin(SimpleHistoryAdmin):
    search_fields = ('client', 'name',)
    list_display = ('client', 'name',)
    # autocomplete_light functionality
    form = CampaignAdminForm

