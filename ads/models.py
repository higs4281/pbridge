from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from shows.models import Show, Episode
from campaigns.models import Campaign
from vendors.models import Vendor, Order


class Ad(TimeStampedModel):
    campaign = models.ForeignKey(Campaign)
    show = models.ForeignKey(Show)
    vendor = models.ForeignKey(Vendor)
    scheduled_date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    projected_views = models.IntegerField(default=0)
    views_guaranteed = models.BooleanField(default=True)
    # Cost Type values:
    FLATRATE = 0
    MAKEGOOD = 1
    BONUS = 2
    CPM = 3
    CPA = 4
    # Cost Type choices (human-readable values):
    COST_TYPE_CHOICES = (
        (FLATRATE, 'Flat Rate'),
        (MAKEGOOD, 'Makegood'),
        (BONUS, 'Bonus'),
        (CPM, 'CPM (actual)'),
        (CPA, 'CPA'),
    )
    # Cost Type Field itself:
    cost_type = models.PositiveSmallIntegerField(
        choices=COST_TYPE_CHOICES,
        default=FLATRATE,
    )
    order = models.ForeignKey(Order, null=True, blank=True)
    instructions = models.TextField('special instructions', blank=True)
    episode = models.ForeignKey(Episode, null=True, blank=True)
    timestamp = models.CharField(max_length=31, blank=True)
    verified = models.BooleanField('drop verified', default=False)
    notes = models.TextField('execution notes', blank=True)
    makegood_needed = models.BooleanField(default=False)
    history = HistoricalRecords()

    @property
    def signed(self):
        order = self.order_set.all()
        return bool(order)

    @property
    def dropped(self):
        if self.episode:
            return self.episode.date <= timezone.now().date()
        return False

    # Display cost with pretty formatting
    @property
    def dollar_amount(self):
        return '$ {:,.0f}'.format(self.cost)

    # Display scheduled date with pretty formatting
    @property
    def scheduled_date_display(self):
        if self.scheduled_date:
            return self.scheduled_date.strftime('%m/%d/%y')
        return None

    def get_absolute_url(self):
        return reverse('ads:detail', args=[str(self.id)])

    def clean(self):
        # Shouldn't have cost if it's a bonus or makegood
        if self.cost_type in (self.MAKEGOOD, self.BONUS) and self.cost > 0:
            msg = "A {} shouldn't have cost.".format(self.get_cost_type_display())
            raise ValidationError(msg)
        if self.verified and not self.dropped:
            msg = "An ad can't be verified if it hasn't dropped."
            raise ValidationError(msg)

    @python_2_unicode_compatible
    def __str__(self):
        if self.scheduled_date:
            return '{} - {} - {:%m/%d/%y}'.format(
                self.show,
                self.vendor,
                self.scheduled_date,
            )
        return '{} - {} - TBD'.format(self.show, self.vendor)

    class Meta:
        ordering = ['-scheduled_date']
