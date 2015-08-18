# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.CharField(max_length=20, unique=True, null=True, blank=True),
        ),
    ]
