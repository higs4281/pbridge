# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalshow',
            name='host_id',
        ),
        migrations.RemoveField(
            model_name='show',
            name='host',
        ),
        migrations.AddField(
            model_name='show',
            name='hosts',
            field=models.ManyToManyField(blank=True, to='shows.Host'),
            preserve_default=True,
        ),
    ]
