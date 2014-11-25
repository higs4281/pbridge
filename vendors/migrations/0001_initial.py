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
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('vendor_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('client_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('insertion_order', models.TextField(max_length=100, verbose_name='signed insertion order', blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('logo', models.TextField(max_length=100, blank=True)),
                ('name_to_clients', models.CharField(max_length=255, verbose_name='default name to clients', help_text='Enter if different from vendor name', blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='order name')),
                ('insertion_order', models.FileField(verbose_name='signed insertion order', upload_to='doc', blank=True)),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
                'ordering': ['-modified'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
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
                ('name', models.CharField(max_length=255, verbose_name='vendor name')),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('logo', models.FileField(upload_to='img', blank=True)),
                ('name_to_clients', models.CharField(max_length=255, verbose_name='default name to clients', help_text='Enter if different from vendor name', blank=True)),
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
