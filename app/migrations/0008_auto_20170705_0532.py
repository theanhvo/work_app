# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170705_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='employee_type',
            field=models.CharField(max_length=100, null=True, verbose_name='Employee_type'),
        ),
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(max_length=7, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='post',
            name='job_feature',
            field=models.CharField(max_length=100, null=True, verbose_name='Job_feature'),
        ),
        migrations.AddField(
            model_name='post',
            name='number_recruits',
            field=models.IntegerField(null=True, verbose_name='Number_recruits'),
        ),
    ]
