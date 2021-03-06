# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20170211_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studies',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Inclusion'),
        ),
        migrations.AlterField(
            model_name='studies',
            name='exclusion',
            field=models.TextField(verbose_name='Exclusion Criteria'),
        ),
        migrations.AlterField(
            model_name='studies',
            name='inclusion',
            field=models.TextField(verbose_name='Inclusion Criteria'),
        ),
        migrations.AlterField(
            model_name='studies',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='studies',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Profile'),
        ),
    ]
