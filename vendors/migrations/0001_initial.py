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
            name='HistoricalOrder',
            fields=[
                ('id', models.IntegerField(blank=True, verbose_name='ID', db_index=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('vendor_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('client_id', models.IntegerField(null=True, blank=True, db_index=True)),
                ('insertion_order', models.TextField(blank=True, max_length=100, verbose_name='signed insertion order')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical order',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalVendor',
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
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(blank=True, max_length=255)),
                ('logo', models.TextField(blank=True, max_length=100)),
                ('name_to_clients', models.CharField(help_text='Enter if different from vendor name', max_length=255, verbose_name='default name to clients', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical vendor',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('insertion_order', models.FileField(blank=True, verbose_name='signed insertion order', upload_to='doc')),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
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
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(blank=True, max_length=255)),
                ('logo', models.FileField(blank=True, upload_to='img')),
                ('name_to_clients', models.CharField(help_text='Enter if different from vendor name', max_length=255, verbose_name='default name to clients', blank=True)),
                ('user', models.ManyToManyField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(to='vendors.Vendor'),
            preserve_default=True,
        ),
    ]
