# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20150321_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalhost',
            name='name',
        ),
        migrations.RemoveField(
            model_name='host',
            name='name',
        ),
        migrations.AddField(
            model_name='historicalhost',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalhost',
            name='last_name',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='last_name',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
