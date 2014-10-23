# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0008_auto_20141015_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewlog',
            name='brew_rating',
            field=models.CharField(default=b'Low', max_length=6, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')]),
        ),
    ]
