# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('shows', '0001_initial'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='episode',
            field=models.ForeignKey(null=True, blank=True, to='shows.Episode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='order',
            field=models.ForeignKey(null=True, blank=True, to='vendors.Order'),
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
