# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=12, verbose_name='\u59d3\u540d')),
                ('identification_number', models.CharField(max_length=18, verbose_name='\u8eab\u4efd\u8bc1\u53f7')),
                ('contact_information', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('ethnic', models.CharField(max_length=20, verbose_name='\u6c11\u65cf')),
                ('birth', models.CharField(max_length=14, verbose_name='\u751f\u65e5')),
                ('marital', models.CharField(choices=[('\u5df2\u5a5a', '\u5df2\u5a5a'), ('\u672a\u5a5a', '\u672a\u5a5a')], max_length=9, verbose_name='\u5a5a\u59fb\u72b6\u6001')),
                ('education', models.CharField(max_length=10, verbose_name='\u6587\u5316\u7a0b\u5ea6')),
                ('account_location', models.CharField(max_length=100, verbose_name='\u6237\u53e3\u5730\u5740')),
                ('we_chat_number', models.CharField(max_length=30, verbose_name='\u5fae\u4fe1\u53f7')),
            ],
            options={
                'verbose_name': '\u4eba\u5458\u4fe1\u606f',
                'verbose_name_plural': '\u4eba\u5458\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='DepartmentInfo',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('departments', models.CharField(default='', max_length=12, verbose_name='\u90e8\u95e8\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u90e8\u95e8\u4fe1\u606f',
                'verbose_name_plural': '\u90e8\u95e8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='PositionInfo',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('positions', models.CharField(default='', max_length=16, verbose_name='\u804c\u4f4d\u540d\u79f0')),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='information.DepartmentInfo')),
            ],
            options={
                'verbose_name': '\u804c\u4f4d\u4fe1\u606f',
                'verbose_name_plural': '\u804c\u4f4d\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.DepartmentInfo')),
                ('name', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.BaseInfo')),
                ('position', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='information.PositionInfo')),
            ],
            options={
                'verbose_name': '\u4fe1\u606f\u6c47\u603b',
                'verbose_name_plural': '\u4fe1\u606f\u6c47\u603b',
            },
        ),
    ]
