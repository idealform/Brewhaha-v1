# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0004_auto_20141015_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewaction',
            name='brewaction_comment',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
