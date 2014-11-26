# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
        ('shows', '0001_initial'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='episode',
            field=models.ForeignKey(null=True, to='shows.Episode', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='order',
            field=models.ForeignKey(null=True, to='vendors.Order', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='show',
            field=models.ForeignKey(to='shows.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='vendor',
            field=models.ForeignKey(to='vendors.Vendor'),
            preserve_default=True,
        ),
    ]
