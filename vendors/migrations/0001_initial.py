# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', auto_created=True, blank=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('vendor_id', models.IntegerField(db_index=True, blank=True, null=True)),
                ('client_id', models.IntegerField(db_index=True, blank=True, null=True)),
                ('insertion_order', models.TextField(verbose_name='signed insertion order', max_length=100, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalVendor',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', auto_created=True, blank=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='phone number', max_length=25, blank=True)),
                ('address_1', models.CharField(verbose_name='address', max_length=63, blank=True)),
                ('address_2', models.CharField(verbose_name='address line 2', max_length=63, blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(verbose_name='zip code', max_length=10, blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('name_to_clients', models.CharField(verbose_name='default name to clients', max_length=255, blank=True, help_text='Enter if different from vendor name')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical vendor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('insertion_order', models.FileField(verbose_name='signed insertion order', upload_to='', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='phone number', max_length=25, blank=True)),
                ('address_1', models.CharField(verbose_name='address', max_length=63, blank=True)),
                ('address_2', models.CharField(verbose_name='address line 2', max_length=63, blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(verbose_name='zip code', max_length=10, blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('name_to_clients', models.CharField(verbose_name='default name to clients', max_length=255, blank=True, help_text='Enter if different from vendor name')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
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
