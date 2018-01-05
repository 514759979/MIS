# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20180105_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionInfo',
            fields=[
                ('positions', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='\u804c\u4f4d\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u804c\u4f4d\u4fe1\u606f',
                'verbose_name_plural': '\u804c\u4f4d\u4fe1\u606f',
            },
        ),
        migrations.RemoveField(
            model_name='departmentinfo',
            name='positions',
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='department',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.DepartmentInfo'),
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='name',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.BaseInfo'),
        ),
        migrations.AddField(
            model_name='positioninfo',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.DepartmentInfo'),
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='position',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.PositionInfo'),
        ),
    ]