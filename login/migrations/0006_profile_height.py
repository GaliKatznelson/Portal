# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
