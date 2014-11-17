from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from clients.models import Client
from shows.mixins import ContactInfoMixin


class Vendor(ContactInfoMixin, TimeStampedModel):
    name = models.CharField('vendor name', max_length=255)
    contact_name = models.CharField(max_length=255, blank=True)
    logo = models.FileField(upload_to='img', blank=True)
    name_to_clients = models.CharField(
        'default name to clients',
        max_length=255,
        blank=True,
        help_text='Enter if different from vendor name',
    )
    user = models.ManyToManyField(User, null=True, blank=True)
    history = HistoricalRecords()

    @python_2_unicode_compatible
    def __str__(self):
        return self.name_to_clients

    def save(self, *args, **kwargs):
        # Default name_to_clients to name
        if not self.name_to_clients:
            self.name_to_clients = self.name
        super(Vendor, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']


class Order(TimeStampedModel):
    name = models.CharField('order name', max_length=255)
    vendor = models.ForeignKey(Vendor)
    client = models.ForeignKey(Client)
    insertion_order = models.FileField('signed insertion order', upload_to='doc', blank=True)
    history = HistoricalRecords()

    @python_2_unicode_compatible
    def __str__(self):
        return self.name