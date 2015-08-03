# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedNTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=255)),
                ('math', models.CharField(max_length=5, null=True, blank=True)),
                ('physics', models.CharField(max_length=5, null=True, blank=True)),
                ('chemistry', models.CharField(max_length=5, null=True, blank=True)),
                ('geometry', models.CharField(max_length=5, null=True, blank=True)),
                ('biology', models.CharField(max_length=5, null=True, blank=True)),
                ('geography', models.CharField(max_length=5, null=True, blank=True)),
                ('history', models.CharField(max_length=5, null=True, blank=True)),
                ('eng_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('ger_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('fr_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('kyr_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('rus_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('uzb_lang', models.CharField(max_length=5, null=True, blank=True)),
                ('informatics', models.CharField(max_length=5, null=True, blank=True)),
                ('civics', models.CharField(max_length=5, null=True, blank=True)),
                ('notes', models.CharField(max_length=5, null=True, blank=True)),
            ],
        ),
    ]
