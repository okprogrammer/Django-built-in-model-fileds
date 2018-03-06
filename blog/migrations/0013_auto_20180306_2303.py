# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180306_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('publish', 'Publish'), ('private', 'Private'), ('draft', 'Draft')], default='draft', max_length=120),
        ),
    ]