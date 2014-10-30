# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '__first__'),
        ('shows', '__first__'),
        ('vendors', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')])),
                ('instructions', models.TextField(blank=True, verbose_name='special instructions')),
                ('timestamp', models.CharField(max_length=31, blank=True)),
                ('verified', models.BooleanField(default=False, verbose_name='drop verified')),
                ('notes', models.TextField(blank=True, verbose_name='execution notes')),
                ('makegood_needed', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
                ('episode', models.ForeignKey(to='shows.Episode', null=True, blank=True)),
                ('order', models.ManyToManyField(null=True, to='vendors.Order', blank=True)),
                ('show', models.ForeignKey(to='shows.Show')),
                ('vendor', models.ForeignKey(to='vendors.Vendor')),
            ],
            options={
                'ordering': ['-scheduled_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalAd',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', blank=True, auto_created=True, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('campaign_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('show_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('vendor_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')])),
                ('instructions', models.TextField(blank=True, verbose_name='special instructions')),
                ('episode_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('timestamp', models.CharField(max_length=31, blank=True)),
                ('verified', models.BooleanField(default=False, verbose_name='drop verified')),
                ('notes', models.TextField(blank=True, verbose_name='execution notes')),
                ('makegood_needed', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'historical ad',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
