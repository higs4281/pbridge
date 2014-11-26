# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
from django.conf import settings
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
                ('id', models.IntegerField(verbose_name='ID', blank=True, auto_created=True, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='order name', max_length=255)),
                ('vendor_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('client_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('insertion_order', models.TextField(verbose_name='signed insertion order', max_length=100, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
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
                ('id', models.IntegerField(verbose_name='ID', blank=True, auto_created=True, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='phone number', max_length=25, blank=True)),
                ('address_1', models.CharField(verbose_name='address', max_length=63, blank=True)),
                ('address_2', models.CharField(verbose_name='address line 2', max_length=63, blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(verbose_name='zip code', max_length=10, blank=True)),
                ('name', models.CharField(verbose_name='vendor name', max_length=255)),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('logo', models.TextField(max_length=100, blank=True)),
                ('name_to_clients', models.CharField(verbose_name='default name to clients', blank=True, max_length=255, help_text='Enter if different from vendor name')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='order name', max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='phone number', max_length=25, blank=True)),
                ('address_1', models.CharField(verbose_name='address', max_length=63, blank=True)),
                ('address_2', models.CharField(verbose_name='address line 2', max_length=63, blank=True)),
                ('city', models.CharField(max_length=63, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(verbose_name='zip code', max_length=10, blank=True)),
                ('name', models.CharField(verbose_name='vendor name', max_length=255)),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('logo', models.FileField(upload_to='img', blank=True)),
                ('name_to_clients', models.CharField(verbose_name='default name to clients', blank=True, max_length=255, help_text='Enter if different from vendor name')),
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
