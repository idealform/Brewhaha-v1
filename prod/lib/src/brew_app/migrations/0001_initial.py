# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrewAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brewaction_time', models.DateTimeField(auto_now_add=True)),
                ('brewaction_step', models.CharField(default=b'NotStarted', max_length=2, choices=[(b'NotStarted', b'Not Started'), (b'MashStarted', b'Mash Started'), (b'MashEnded', b'Mash Ended'), (b'st', b'Sparge Started'), (b'se', b'Sparge Ended'), (b'bs', b'Boil Started'), (b'be', b'Boil Ended'), (b'fs', b'Fermentation Started'), (b'fe', b'Fermentation Ended'), (b'bs', b'Bottled'), (b'be', b'Completed')])),
                ('brewaction_comment', models.CharField(max_length=80, unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrewLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brew_name', models.CharField(max_length=80, null=True)),
                ('brew_start_time', models.DateTimeField(auto_now_add=True)),
                ('brew_end_time', models.DateTimeField(auto_now_add=True)),
                ('brew_rating', models.CharField(default=b'lo', max_length=2, choices=[(b'lo', b'Low'), (b'me', b'Medium'), (b'hi', b'High')])),
                ('brew_status', models.CharField(default=b'bs', max_length=2, choices=[(b'bs', b'Brew Started'), (b'be', b'Brew Ended'), (b'fs', b'Fermentation Started'), (b'fe', b'Fermentation Ended'), (b'bs', b'Bottling Started'), (b'be', b'Completed')])),
                ('brew_action', models.ManyToManyField(to='brew_app.BrewAction', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrainIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amountof_grain', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrainList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grain_name', models.CharField(max_length=60, unique=True, null=True)),
                ('grain_gravity', models.IntegerField(null=True)),
                ('grain_description', models.CharField(max_length=80, null=True)),
                ('grainlist_type', models.CharField(default=b'ag', max_length=2, choices=[(b'ag', b'All Grain'), (b'ex', b'Extract')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HopIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amountof_hops', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HopList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hop_name', models.CharField(max_length=60, unique=True, null=True)),
                ('hop_alpha', models.IntegerField(null=True)),
                ('hoplist_origin', models.CharField(default=b'us', max_length=2, choices=[(b'us', b'US'), (b'uk', b'UK'), (b'ge', b'Germany'), (b'ca', b'Canada'), (b'po', b'Poland'), (b'nz', b'New Zealand'), (b'au', b'Australia'), (b'cr', b'Czech Rep'), (b'fr', b'France'), (b'sl', b'Slovenia')])),
                ('hoplist_type', models.CharField(default=b'ar', max_length=2, choices=[(b'ar', b'Aroma'), (b'bi', b'Bittering')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_name', models.CharField(max_length=80, unique=True, null=True)),
                ('recipe_type', models.CharField(default=b'ag', max_length=2, choices=[(b'ag', b'All Grain'), (b'ex', b'Extract')])),
                ('recipe_grain', models.ManyToManyField(to='brew_app.GrainIngredient', null=True)),
                ('recipe_hop', models.ManyToManyField(to='brew_app.HopIngredient', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YeastIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amountof_yeast', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YeastList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yeast_name', models.CharField(max_length=60, unique=True, null=True)),
                ('hoplist_origin', models.CharField(default=b'al', max_length=2, choices=[(b'al', b'Ale'), (b'ch', b'Champagne'), (b'la', b'Lager'), (b'wh', b'Wheat'), (b'wi', b'Wine')])),
                ('yeastlist_floc', models.CharField(default=b'lo', max_length=2, choices=[(b'lo', b'Low'), (b'me', b'Medium'), (b'hi', b'High')])),
                ('yeastlist_type', models.CharField(default=b'dr', max_length=2, choices=[(b'dr', b'Dry'), (b'li', b'Liquid')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='yeastingredient',
            name='selected_yeast',
            field=models.ForeignKey(to='brew_app.YeastList', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_yeast',
            field=models.ManyToManyField(to='brew_app.YeastIngredient', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hopingredient',
            name='selected_hops',
            field=models.ForeignKey(to='brew_app.HopList', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grainingredient',
            name='selected_grain',
            field=models.ForeignKey(to='brew_app.GrainList', null=True),
            preserve_default=True,
        ),
    ]
