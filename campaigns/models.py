from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from clients.models import Client, Budget


class Campaign(TimeStampedModel):
    name = models.CharField('campaign name', max_length=255)
    client = models.ForeignKey(Client)
    budget = models.ForeignKey(Budget)
    description = models.TextField(blank=True)
    history = HistoricalRecords()

    @property
    def planned_spend(self):
        return self.ad_set.sum('cost')

    @property
    def planned_spend_display(self):
        return '$ {:,.0f}'.format(self.planned_spend)

    @python_2_unicode_compatible
    def __str__(self):
        return '{} - {}'.format(self.client, self.name)

    def get_absolute_url(self):
        return reverse('campaigns:detail', args=[str(self.id)])