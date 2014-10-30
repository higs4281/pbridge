# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='phone number')),
                ('address_1', models.CharField(blank=True, max_length=63, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=63, verbose_name='address line 2')),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(blank=True, max_length=10, verbose_name='zip code')),
                ('name', models.CharField(max_length=255, verbose_name='client name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalBudget',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, blank=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('client_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical budget',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, blank=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='phone number')),
                ('address_1', models.CharField(blank=True, max_length=63, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=63, verbose_name='address line 2')),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(blank=True, max_length=10, verbose_name='zip code')),
                ('name', models.CharField(max_length=255, verbose_name='client name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical client',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='budget',
            name='client',
            field=models.ForeignKey(to='clients.Client'),
            preserve_default=True,
        ),
    ]
