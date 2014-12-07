from __future__ import absolute_import, unicode_literals
from import_export import resources

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Show, Episode, Tracking, Platform, Host
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
    search_fields = ('name',)
    list_display = ('name', 'default_vendor')

    # autocomplete_light functionality
    form = ShowAdminForm

    inlines = [TrackingInline, EpisodeInline]


@admin.register(Episode)
class EpisodeAdmin(SimpleHistoryAdmin):
    list_display = ('show', 'date', 'link',)
    fields = ('show', 'date',)


admin.site.register(Platform)
admin.site.register(Host)


class ShowResource(resources.ModelResource):
    """
    Base resource for Show Import/Export.
    """

    class Meta:
        model = Show
        fields = [
            'name',
            'host__name',
            'host__email',
            'api_id',
            'platform__name',
            'art_external',
            'description',
            'link',
            'feed',
            'episodes_per_month',
            'downloads_per_episode',
            'default_vendor__name',
            'active',
            'history',
        ]