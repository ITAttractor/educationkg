# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntc', '0002_auto_20150807_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parsedntc',
            name='integrated',
        ),
    ]
