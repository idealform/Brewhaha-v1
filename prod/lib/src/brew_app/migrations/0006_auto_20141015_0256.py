# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0005_auto_20141015_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewaction',
            name='brewaction_step',
            field=models.CharField(default=b'Not Started', max_length=15, choices=[(b'Not Started', b'Not Started'), (b'Mash Started', b'Mash Started'), (b'Mash Ended', b'Mash Ended'), (b'Sparge Started', b'Sparge Started'), (b'Sparge Ended', b'Sparge Ended'), (b'Boil Started', b'Boil Started'), (b'Boil Ended', b'Boil Ended'), (b'Fermentation Started', b'Fermentation Started'), (b'Fermentation Ended', b'Fermentation Ended'), (b'Bottled', b'Bottled'), (b'Completed', b'Completed')]),
        ),
    ]
