from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from shows.mixins import ContactInfoMixin


class Client(ContactInfoMixin, TimeStampedModel):
    name = models.CharField('client name', max_length=255)
    contact_name = models.CharField(max_length=255, blank=True)
    logo = models.FileField(upload_to='img', blank=True)
    history = HistoricalRecords()

    @python_2_unicode_compatible
    def __str__(self):
        return self.name


class Budget(TimeStampedModel):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    history = HistoricalRecords()

    @property
    def dollar_amount(self):
        return '$ {:,.0f}'.format(self.amount)

    @python_2_unicode_compatible
    def __str__(self):
        return '{} - $ {:,.0f}'.format(self.name, self.amount)