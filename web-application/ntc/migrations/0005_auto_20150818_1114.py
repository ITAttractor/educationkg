# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntc', '0004_auto_20150818_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntc',
            name='biology',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Biology', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='chemistry',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Chemistry', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='civics',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Civics', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='eng_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='English language', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='fr_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='French language', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='geography',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Geography', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='geometry',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Geometry', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='ger_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='German language', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='history',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='History', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='informatics',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Informatics', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='kyr_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Kyrgyz language', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='notes',
            field=models.CharField(max_length=5, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='physics',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Physics', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='rus_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Russian language', blank=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='uzb_lang',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Uzbek language', blank=True),
        ),
    ]
