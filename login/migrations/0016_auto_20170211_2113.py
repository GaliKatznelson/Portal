# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20170211_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studies',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='studies',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
