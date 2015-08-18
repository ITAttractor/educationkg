# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntc', '0003_remove_parsedntc_integrated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntc',
            name='math',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Math', blank=True),
        ),
    ]
