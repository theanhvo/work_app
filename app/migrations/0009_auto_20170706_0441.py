# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170705_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='employee_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='position',
        ),
        migrations.AddField(
            model_name='post',
            name='experience',
            field=models.CharField(max_length=36, null=True, verbose_name='Experience'),
        ),
        migrations.AddField(
            model_name='post',
            name='type_job',
            field=models.CharField(max_length=100, null=True, verbose_name='Type_job'),
        ),
        migrations.AlterField(
            model_name='post',
            name='employer_mail',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Employer_mail'),
        ),
    ]
