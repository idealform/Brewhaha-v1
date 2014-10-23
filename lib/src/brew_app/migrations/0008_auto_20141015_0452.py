# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brew_app', '0007_auto_20141015_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewaction',
            name='brewaction_step',
            field=models.CharField(default=b'Not Started', max_length=20, choices=[(b'Not Started', b'Not Started'), (b'Mash Started', b'Mash Started'), (b'Mash Ended', b'Mash Ended'), (b'Sparge Started', b'Sparge Started'), (b'Sparge Ended', b'Sparge Ended'), (b'Boil Started', b'Boil Started'), (b'Boil Ended', b'Boil Ended'), (b'Fermentation Started', b'Fermentation Started'), (b'Fermentation Ended', b'Fermentation Ended'), (b'Bottled', b'Bottled'), (b'Completed', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='brewlog',
            name='brew_status',
            field=models.CharField(default=b'Brew Started', max_length=20, choices=[(b'Brew Started', b'Brew Started'), (b'Brew Ended', b'Brew Ended'), (b'Fermentation Started', b'Fermentation Started'), (b'Fermentation ended', b'Fermentation Ended'), (b'Bottled', b'Bottled Started'), (b'Completed', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='grainlist',
            name='grainlist_type',
            field=models.CharField(default=b'All Graing', max_length=9, choices=[(b'All Graing', b'All Grain'), (b'Extract', b'Extract')]),
        ),
        migrations.AlterField(
            model_name='hoplist',
            name='hoplist_origin',
            field=models.CharField(default=b'US', max_length=15, choices=[(b'US', b'US'), (b'UK', b'UK'), (b'Germany', b'Germany'), (b'Canada', b'Canada'), (b'Poland', b'Poland'), (b'New Zealand', b'New Zealand'), (b'Australia', b'Australia'), (b'Czech Republic', b'Czech Rep'), (b'France', b'France'), (b'Slovenia', b'Slovenia')]),
        ),
        migrations.AlterField(
            model_name='hoplist',
            name='hoplist_type',
            field=models.CharField(default=b'Aroma', max_length=10, choices=[(b'Aroma', b'Aroma'), (b'Bittering', b'Bittering')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(default=b'All Grain', max_length=9, choices=[(b'All Grain', b'All Grain'), (b'Extract', b'Extract')]),
        ),
        migrations.AlterField(
            model_name='yeastlist',
            name='hoplist_origin',
            field=models.CharField(default=b'Ale', max_length=10, choices=[(b'Ale', b'Ale'), (b'Champagne', b'Champagne'), (b'Lager', b'Lager'), (b'Wheat', b'Wheat'), (b'Wine', b'Wine')]),
        ),
        migrations.AlterField(
            model_name='yeastlist',
            name='yeastlist_floc',
            field=models.CharField(default=b'Low', max_length=6, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')]),
        ),
        migrations.AlterField(
            model_name='yeastlist',
            name='yeastlist_type',
            field=models.CharField(default=b'Dry', max_length=6, choices=[(b'Dry', b'Dry'), (b'Liquid', b'Liquid')]),
        ),
    ]
