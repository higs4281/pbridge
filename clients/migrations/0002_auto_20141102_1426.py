# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='logo',
            field=models.FileField(default='', upload_to='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalclient',
            name='logo',
            field=models.TextField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
