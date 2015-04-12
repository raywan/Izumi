# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150411_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=6),
            preserve_default=True,
        ),
    ]
