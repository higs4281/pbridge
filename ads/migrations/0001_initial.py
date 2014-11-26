# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(max_digits=12, default=0.0, decimal_places=2)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')], default=0)),
                ('instructions', models.TextField(verbose_name='special instructions', blank=True)),
                ('timestamp', models.CharField(max_length=31, blank=True)),
                ('verified', models.BooleanField(verbose_name='drop verified', default=False)),
                ('notes', models.TextField(verbose_name='execution notes', blank=True)),
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
                ('id', models.IntegerField(verbose_name='ID', blank=True, auto_created=True, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('campaign_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('show_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('vendor_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('cost', models.DecimalField(max_digits=12, default=0.0, decimal_places=2)),
                ('projected_views', models.IntegerField(default=0)),
                ('views_guaranteed', models.BooleanField(default=True)),
                ('cost_type', models.PositiveSmallIntegerField(choices=[(0, 'Flat Rate'), (1, 'Makegood'), (2, 'Bonus'), (3, 'CPM (actual)'), (4, 'CPA')], default=0)),
                ('order_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('instructions', models.TextField(verbose_name='special instructions', blank=True)),
                ('episode_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('timestamp', models.CharField(max_length=31, blank=True)),
                ('verified', models.BooleanField(verbose_name='drop verified', default=False)),
                ('notes', models.TextField(verbose_name='execution notes', blank=True)),
                ('makegood_needed', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ad',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
