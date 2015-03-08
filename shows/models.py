from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.conf import settings

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords

from clients.models import Client
from vendors.models import Vendor
from .mixins import ContactInfoMixin
from . import apitools


class Platform(TimeStampedModel):
    # Setting to hook API functionality into a platform object
    CLASS_DICT = {
        # platform.id: class
        1: apitools.YouTubeAPI,
        2: apitools.ItunesAPI,
    }
    name = models.CharField('platform name', max_length=255)
    simple_name = models.CharField('simplified name', max_length=63)
    show_base_url = models.CharField(
        'base url for shows',
        max_length=255,
        help_text='use brackets as id placeholder, e.g. example.com/show/{{}}/',
    )
    episode_base_url = models.CharField(
        'base url for episodes',
        max_length=255,
        help_text='use brackets as id placeholder, e.g. site.com/episode/{{}}/',
    )
    content_type = models.CharField(max_length=63)

    def get_api_class(self):
        return self.CLASS_DICT.get(self.id)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Currently treating simple_name as a fake SlugField; consider
        # changing to an actual SlugField.
        if self.simple_name:
            self.simple_name = slugify(self.simple_name)
        else:
            self.simple_name = slugify(self.name)
        super(Platform, self).save(*args, **kwargs)


class Host(ContactInfoMixin, TimeStampedModel):
    name = models.CharField('host name', max_length=255)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('shows:host_detail', args=[str(self.id)])

    @python_2_unicode_compatible
    def __str__(self):
        return self.name


class Show(TimeStampedModel):
    name = models.CharField('show name', max_length=255)
    host = models.ForeignKey(Host, null=True, blank=True)
    # hosts = models.ManyToManyField(Host, blank=True)
    api_id = models.CharField('API id', max_length=255, blank=True)
    platform = models.ForeignKey(Platform)
    tags = TaggableManager(blank=True)
    art_height = models.PositiveSmallIntegerField(blank=True, null=True)
    art_width = models.PositiveSmallIntegerField(blank=True, null=True)
    art_external = models.URLField('splash art URL', blank=True)
    art_file = models.ImageField(
        'splash art file',
        upload_to='img',
        blank=True,
        width_field='art_width',
        height_field='art_height',
    )
    description = models.TextField('show description', blank=True)
    link = models.URLField('show page URL', blank=True)
    feed = models.URLField('RSS Feed URL', blank=True)
    episodes_per_month = models.PositiveSmallIntegerField(default=1)
    downloads_per_episode = models.PositiveIntegerField(default=0)
    default_vendor = models.ForeignKey(Vendor, null=True, blank=True)
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    history = HistoricalRecords()

    @property
    def homepage(self):
        return self.platform.show_base_url.format(self.api_id)

    def get_absolute_url(self):
        return reverse('shows:detail', args=[str(self.id)])

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Episode(TimeStampedModel):
    show = models.ForeignKey(Show)
    date = models.DateField('episode date')
    link = models.URLField('episode URL', max_length=255, blank=True)
    downloads = models.IntegerField('unique downloads', default=0)
    details = models.CharField(max_length=255, blank=True)
    api_id = models.CharField('API id', max_length=255, blank=True)
    history = HistoricalRecords()

    @property
    def is_recent(self):
        today = timezone.now().date()
        d = timedelta(days=90)
        return (today - d) <= self.date <= (today + d)

    @python_2_unicode_compatible
    def __str__(self):
        return '{} - {:%m/%d/%Y}'.format(self.show.name, self.date)

    class Meta:
        ordering = ['-date']


class Tracking(TimeStampedModel):
    show = models.ForeignKey(Show)
    client = models.ForeignKey(Client)
    # Tracking type values
    URL = 1
    PROMO = 2
    # Tracking type choices & human readable labels
    TRACKING_TYPE_CHOICES = (
        (URL, 'URL'),
        (PROMO, 'Promo Code'),
    )
    # The type field itself
    tracking_type = models.PositiveSmallIntegerField(
        choices=TRACKING_TYPE_CHOICES,
        default=URL,
    )
    tracking = models.CharField(max_length=255, blank=True)
    verified = models.BooleanField('tracking verified', default=False)
    history = HistoricalRecords()

    @python_2_unicode_compatible
    def __str__(self):
        return self.tracking
