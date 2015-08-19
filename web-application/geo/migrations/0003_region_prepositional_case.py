# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_region_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='prepositional_case',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
