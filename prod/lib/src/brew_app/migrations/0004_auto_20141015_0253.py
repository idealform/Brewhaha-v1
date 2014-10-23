# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0003_auto_20141015_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewaction',
            name='brewaction_step',
            field=models.CharField(default=b'Not Started', max_length=15, choices=[(b'Not Started', b'Not Started'), (b'Mash_Started', b'Mash Started'), (b'Mash Ended', b'Mash Ended'), (b'st', b'Sparge Started'), (b'se', b'Sparge Ended'), (b'bs', b'Boil Started'), (b'be', b'Boil Ended'), (b'fs', b'Fermentation Started'), (b'fe', b'Fermentation Ended'), (b'bs', b'Bottled'), (b'be', b'Completed')]),
        ),
    ]
