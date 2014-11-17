from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.ShowListView.as_view(), name='index'),
    url(r'^orders/create/$', views.OrderCreateView.as_view(), name='order_create'),
]
