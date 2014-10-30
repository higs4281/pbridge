# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='campaign name')),
                ('description', models.TextField(blank=True)),
                ('budget', models.ForeignKey(to='clients.Budget')),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCampaign',
            fields=[
                ('id', models.IntegerField(auto_created=True, verbose_name='ID', db_index=True, blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='campaign name')),
                ('client_id', models.IntegerField(db_index=True, blank=True, null=True)),
                ('budget_id', models.IntegerField(db_index=True, blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'historical campaign',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
