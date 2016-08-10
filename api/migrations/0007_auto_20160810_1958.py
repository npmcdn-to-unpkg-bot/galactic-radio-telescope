# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-10 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_galaxyinstance_norm_users_recent'),
    ]

    operations = [
        migrations.AddField(
            model_name='galaxyinstance',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='galaxyinstance',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]