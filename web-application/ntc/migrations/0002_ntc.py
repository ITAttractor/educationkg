# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('schools', '0001_initial'),
        ('ntc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('district', models.ForeignKey(to='geo.District')),
                ('school', models.ForeignKey(to='schools.School')),
            ],
        ),
    ]
