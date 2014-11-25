# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import taggit.managers
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('date', models.DateField(verbose_name='episode date')),
                ('link', models.URLField(max_length=255, verbose_name='episode URL', blank=True)),
                ('downloads', models.IntegerField(verbose_name='unique downloads', default=0)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('api_id', models.CharField(max_length=255, verbose_name='API id', blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalEpisode',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('show_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('date', models.DateField(verbose_name='episode date')),
                ('link', models.URLField(max_length=255, verbose_name='episode URL', blank=True)),
                ('downloads', models.IntegerField(verbose_name='unique downloads', default=0)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('api_id', models.CharField(max_length=255, verbose_name='API id', blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(max_length=25, verbose_name='phone number', blank=True)),
                ('address_1', models.CharField(max_length=63, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=63, verbose_name='address line 2', blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(max_length=10, verbose_name='zip code', blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='host name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='show name')),
                ('host_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('api_id', models.CharField(max_length=255, verbose_name='API id', blank=True)),
                ('platform_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('art', models.TextField(max_length=100, verbose_name='splash art', blank=True)),
                ('description', models.TextField(verbose_name='show description', blank=True)),
                ('link', models.URLField(verbose_name='show page URL', blank=True)),
                ('feed', models.URLField(null=True, verbose_name='RSS Feed URL', blank=True)),
                ('episodes_per_month', models.PositiveSmallIntegerField(default=1)),
                ('downloads_per_episode', models.PositiveIntegerField(default=0)),
                ('default_vendor_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('show_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('client_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('tracking_type', models.PositiveSmallIntegerField(choices=[(1, 'URL'), (2, 'Promo Code')], default=1)),
                ('tracking', models.CharField(max_length=255, blank=True)),
                ('verified', models.BooleanField(verbose_name='tracking verified', default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(max_length=25, verbose_name='phone number', blank=True)),
                ('address_1', models.CharField(max_length=63, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=63, verbose_name='address line 2', blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(max_length=10, verbose_name='zip code', blank=True)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='platform name')),
                ('simple_name', models.CharField(max_length=63, verbose_name='simplified name')),
                ('show_base_url', models.CharField(max_length=255, verbose_name='base url for shows', help_text='use brackets as id placeholder, e.g. example.com/show/{{}}/')),
                ('episode_base_url', models.CharField(max_length=255, verbose_name='base url for episodes', help_text='use brackets as id placeholder, e.g. site.com/episode/{{}}/')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='show name')),
                ('api_id', models.CharField(max_length=255, verbose_name='API id', blank=True)),
                ('art', models.ImageField(verbose_name='splash art', upload_to='img', blank=True)),
                ('description', models.TextField(verbose_name='show description', blank=True)),
                ('link', models.URLField(verbose_name='show page URL', blank=True)),
                ('feed', models.URLField(null=True, verbose_name='RSS Feed URL', blank=True)),
                ('episodes_per_month', models.PositiveSmallIntegerField(default=1)),
                ('downloads_per_episode', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('default_vendor', models.ForeignKey(null=True, blank=True, to='vendors.Vendor')),
                ('host', models.ForeignKey(null=True, blank=True, to='shows.Host')),
                ('platform', models.ForeignKey(to='shows.Platform')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', blank=True, through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('tracking_type', models.PositiveSmallIntegerField(choices=[(1, 'URL'), (2, 'Promo Code')], default=1)),
                ('tracking', models.CharField(max_length=255, blank=True)),
                ('verified', models.BooleanField(verbose_name='tracking verified', default=False)),
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
