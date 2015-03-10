from __future__ import absolute_import

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from ads.models import Ad
from .models import Vendor, Order
from .forms import OrderAdminForm


class AdInline(admin.TabularInline):
    model = Ad
    extra = 1


@admin.register(Vendor)
class VendorAdmin(SimpleHistoryAdmin):
    search_fields = ('name', 'name_to_clients', 'contact_name',)


@admin.register(Order)
class OrderAdmin(SimpleHistoryAdmin):
    search_fields = ('name', 'vendor', 'client',)
    # autocomplete_light functionality
    form = OrderAdminForm
    inlines = [AdInline]
