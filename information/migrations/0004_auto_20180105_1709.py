# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_auto_20180105_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninfo',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='information.DepartmentInfo'),
        ),
    ]
