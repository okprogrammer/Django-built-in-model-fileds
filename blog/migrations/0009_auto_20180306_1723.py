# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180306_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('private', 'Private'), ('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=120),
        ),
    ]
