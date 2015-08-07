# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrationQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='NotIntegratedNTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='NTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255)),
                ('math', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('physics', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('chemistry', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('geometry', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('biology', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('geography', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('history', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('eng_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ger_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('fr_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('kyr_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('rus_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('uzb_lang', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('informatics', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('civics', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('notes', models.CharField(max_length=5, null=True, blank=True)),
            ],
        ),
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
                ('integration_queue', models.ForeignKey(to='ntc.IntegrationQueue')),
            ],
        ),
        migrations.AddField(
            model_name='ntc',
            name='parsed_ntc',
            field=models.OneToOneField(to='ntc.ParsedNTC'),
        ),
        migrations.AddField(
            model_name='ntc',
            name='school',
            field=models.ForeignKey(to='schools.School'),
        ),
        migrations.AddField(
            model_name='notintegratedntc',
            name='parsed_ntc',
            field=models.ForeignKey(to='ntc.ParsedNTC'),
        ),
    ]
