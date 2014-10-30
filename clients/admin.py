from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Client, Budget
from .forms import ClientAdminForm, BudgetAdminForm


@admin.register(Client)
class ClientAdmin(SimpleHistoryAdmin):
    search_fields = ('name', 'contact_name',)
    list_display = ('name', )
    # autocomplete_light functionality
    form = ClientAdminForm


@admin.register(Budget)
class BudgetAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'dollar_amount')
    form = BudgetAdminForm