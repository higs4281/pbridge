# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='campaign name')),
                ('description', models.TextField(blank=True)),
                ('budget', models.ForeignKey(to='clients.Budget')),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
                'ordering': ['-modified'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCampaign',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='campaign name')),
                ('client_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('budget_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical campaign',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
