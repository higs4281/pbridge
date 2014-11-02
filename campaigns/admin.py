from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from ads.models import Ad
from .models import Campaign
from .forms import CampaignAdminForm


class AdInLine(admin.TabularInline):
    model = Ad
    extra = 1
    fields = [
        'show',
        'vendor',
        'scheduled_date',
        'cost_type',
        'cost',
        'projected_views',
    ]


@admin.register(Campaign)
class CampaignAdmin(SimpleHistoryAdmin):
    search_fields = ('client', 'name',)
    list_display = ('client', 'name',)

    # autocomplete_light functionality
    form = CampaignAdminForm

    inlines = [AdInLine, ]

