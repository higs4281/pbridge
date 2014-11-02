from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Show, Episode, Tracking, Platform
from .forms import ShowAdminForm


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class TrackingInline(admin.TabularInline):
    model = Tracking
    extra = 1
    verbose_name_plural = "Tracking info"


@admin.register(Show)
class ShowAdmin(SimpleHistoryAdmin):
    search_fields = ('name', 'host', 'default_vendor')
    list_display = ('name', 'default_vendor')

    # autocomplete_light functionality
    form = ShowAdminForm

    inlines = [TrackingInline, EpisodeInline]


@admin.register(Episode)
class EpisodeAdmin(SimpleHistoryAdmin):
    list_display = ('show', 'date', 'link',)
    fields = ('show', 'date',)


admin.site.register(Platform)