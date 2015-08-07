# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notintegratedntc',
            name='parsed_ntc',
        ),
        migrations.AddField(
            model_name='parsedntc',
            name='integrated',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='NotIntegratedNTC',
        ),
    ]
