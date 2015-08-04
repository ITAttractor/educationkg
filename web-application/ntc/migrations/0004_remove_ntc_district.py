# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntc', '0003_auto_20150803_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ntc',
            name='district',
        ),
    ]
