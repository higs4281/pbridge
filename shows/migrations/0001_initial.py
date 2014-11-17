# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('clients', '0001_initial'),
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField(verbose_name='episode date')),
                ('link', models.URLField(blank=True, max_length=255, verbose_name='episode URL')),
                ('downloads', models.IntegerField(default=0, verbose_name='unique downloads')),
                ('details', models.CharField(blank=True, max_length=255)),
                ('api_id', models.CharField(blank=True, max_length=255, verbose_name='API id')),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalEpisode',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('show_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('date', models.DateField(verbose_name='episode date')),
                ('link', models.URLField(blank=True, max_length=255, verbose_name='episode URL')),
                ('downloads', models.IntegerField(default=0, verbose_name='unique downloads')),
                ('details', models.CharField(blank=True, max_length=255)),
                ('api_id', models.CharField(blank=True, max_length=255, verbose_name='API id')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical episode',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalHost',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='phone number')),
                ('address_1', models.CharField(blank=True, max_length=63, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=63, verbose_name='address line 2')),
                ('city', models.CharField(blank=True, max_length=63)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=10, verbose_name='zip code')),
                ('name', models.CharField(max_length=255, verbose_name='host name')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical host',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalShow',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='show name')),
                ('host_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('api_id', models.CharField(blank=True, max_length=255, verbose_name='API id')),
                ('platform_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('art', models.URLField(blank=True, verbose_name='splash art URL')),
                ('description', models.TextField(blank=True, verbose_name='show description')),
                ('link', models.URLField(blank=True, verbose_name='show page URL')),
                ('feed', models.URLField(null=True, blank=True, verbose_name='RSS Feed URL')),
                ('episodes_per_month', models.PositiveSmallIntegerField(default=1)),
                ('downloads_per_episode', models.PositiveIntegerField(default=0)),
                ('default_vendor_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical show',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTracking',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('show_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('client_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('tracking_type', models.PositiveSmallIntegerField(default=1, choices=[(1, 'URL'), (2, 'Promo Code')])),
                ('tracking', models.CharField(blank=True, max_length=255)),
                ('verified', models.BooleanField(default=False, verbose_name='tracking verified')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical tracking',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='phone number')),
                ('address_1', models.CharField(blank=True, max_length=63, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=63, verbose_name='address line 2')),
                ('city', models.CharField(blank=True, max_length=63)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=10, verbose_name='zip code')),
                ('name', models.CharField(max_length=255, verbose_name='host name')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='platform name')),
                ('simple_name', models.CharField(max_length=63, verbose_name='simplified name')),
                ('show_base_url', models.CharField(help_text='use brackets as id placeholder, e.g. example.com/show/{{}}/', max_length=255, verbose_name='base url for shows')),
                ('episode_base_url', models.CharField(help_text='use brackets as id placeholder, e.g. site.com/episode/{{}}/', max_length=255, verbose_name='base url for episodes')),
                ('content_type', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='show name')),
                ('api_id', models.CharField(blank=True, max_length=255, verbose_name='API id')),
                ('art', models.URLField(blank=True, verbose_name='splash art URL')),
                ('description', models.TextField(blank=True, verbose_name='show description')),
                ('link', models.URLField(blank=True, verbose_name='show page URL')),
                ('feed', models.URLField(null=True, blank=True, verbose_name='RSS Feed URL')),
                ('episodes_per_month', models.PositiveSmallIntegerField(default=1)),
                ('downloads_per_episode', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('default_vendor', models.ForeignKey(null=True, to='vendors.Vendor', blank=True)),
                ('host', models.ForeignKey(null=True, to='shows.Host', blank=True)),
                ('platform', models.ForeignKey(to='shows.Platform')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', blank=True, verbose_name='Tags')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('tracking_type', models.PositiveSmallIntegerField(default=1, choices=[(1, 'URL'), (2, 'Promo Code')])),
                ('tracking', models.CharField(blank=True, max_length=255)),
                ('verified', models.BooleanField(default=False, verbose_name='tracking verified')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('show', models.ForeignKey(to='shows.Show')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(to='shows.Show'),
            preserve_default=True,
        ),
    ]
