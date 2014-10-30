from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Ad
from .forms import AdAdminForm

@admin.register(Ad)
class AdAdmin(SimpleHistoryAdmin):
    search_fields = ('campaign', 'episode__show', 'get_date')
    list_display = ('campaign', 'get_show', 'get_date', 'dollar_amount',)

    # Add a way for list_display to use episode attributes
    def get_show(self, obj):
        return obj.episode.show

    get_show.short_description = 'Show Name'

    def get_date(self, obj):
        return obj.episode.date

    get_date.short_description = 'Date'

    # autocomplete_light functionality
    form = AdAdminForm

