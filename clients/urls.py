from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import BudgetCreateView, ClientListView

urlpatterns = [
    url(r'^$', ClientListView.as_view(), name='index'),
    url(
        r'^budgets/create/$',
        BudgetCreateView.as_view(),
        name='budget_create'
    ),
]
