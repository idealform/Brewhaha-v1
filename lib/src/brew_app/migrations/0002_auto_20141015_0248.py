# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewaction',
            name='brewaction_step',
            field=models.CharField(default=b'NotStarted', max_length=15, choices=[(b'NotStarted', b'Not Started'), (b'MashStarted', b'Mash Started'), (b'MashEnded', b'Mash Ended'), (b'st', b'Sparge Started'), (b'se', b'Sparge Ended'), (b'bs', b'Boil Started'), (b'be', b'Boil Ended'), (b'fs', b'Fermentation Started'), (b'fe', b'Fermentation Ended'), (b'bs', b'Bottled'), (b'be', b'Completed')]),
        ),
    ]
