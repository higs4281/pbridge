# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')])),
                ('instructions', models.TextField(blank=True, verbose_name='special instructions')),
                ('timestamp', models.CharField(blank=True, max_length=31)),
                ('verified', models.BooleanField(default=False, verbose_name='drop verified')),
                ('notes', models.TextField(blank=True, verbose_name='execution notes')),
                ('makegood_needed', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
                'ordering': ['-scheduled_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalAd',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('campaign_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('show_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('vendor_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')])),
                ('order_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('instructions', models.TextField(blank=True, verbose_name='special instructions')),
                ('episode_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('timestamp', models.CharField(blank=True, max_length=31)),
                ('verified', models.BooleanField(default=False, verbose_name='drop verified')),
                ('notes', models.TextField(blank=True, verbose_name='execution notes')),
                ('makegood_needed', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ad',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
