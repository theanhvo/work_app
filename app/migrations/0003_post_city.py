# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170702_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
    ]
