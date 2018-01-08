# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


DEPARTMENTS = (
    (u"编辑部", u"编辑部"),
    (u"财务部", u"财务部"),
    (u"泛群部", u"泛群部"),
    (u"群控部", u"群控部"),
    (u"商务部", u"商务部"),
    (u"手机部", u"手机部"),
    (u"投放部", u"投放部"),
    (u"原创部", u"原创部"),
    (u"运营部", u"运营部"),
    (u"综合部", u"综合部"),
    (u"总经办", u"总经办"),
)

MARITAL_STATUS = (
    (u'已婚', u'已婚'),
    (u'未婚', u'未婚'),
)


class PositionInfo(models.Model):
    position_id = models.AutoField(primary_key=True)
    positions = models.CharField(max_length=16, verbose_name=u'职位名称', default='')
    department = models.ForeignKey('DepartmentInfo', default='')

    class Meta:
        verbose_name = u'职位信息'
        verbose_name_plural = u'职位信息'

    def __str__(self):
        return self.positions.encode('utf-8')


class DepartmentInfo(models.Model):
    department_id = models.AutoField(primary_key=True)
    departments = models.CharField(max_length=12, verbose_name=u'部门名称', default='')

    class Meta:
        verbose_name = u'部门信息'
        verbose_name_plural = u'部门信息'

    def __str__(self):
        return self.departments.encode('utf-8')


class BaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12, verbose_name=u'姓名')
    identification_number = models.CharField(max_length=18, verbose_name=u'身份证号')
    contact_information = models.CharField(max_length=11, verbose_name=u'联系方式')
    ethnic = models.CharField(max_length=20, verbose_name=u'民族')
    birth = models.CharField(max_length=14, verbose_name=u'生日')
    marital = models.CharField(max_length=9, verbose_name=u'婚姻状态', choices=MARITAL_STATUS)
    education = models.CharField(max_length=10, verbose_name=u'文化程度')
    account_location = models.CharField(max_length=100, verbose_name=u'户口地址')
    we_chat_number = models.CharField(max_length=30, verbose_name=u'微信号')

    class Meta:
        verbose_name = u'人员信息'
        verbose_name_plural = u'人员信息'

    def __str__(self):
        return self.name.encode('utf-8')


class StaffInfo(models.Model):
    name = models.ForeignKey(BaseInfo, blank=True, default='', verbose_name=u'姓名')
    department = models.ForeignKey(DepartmentInfo, blank=True, default='', verbose_name=u'所在部门')
    position = models.ForeignKey(PositionInfo, blank=True, default='', verbose_name=u'职位')

    class Meta:
        verbose_name = u'信息汇总'
        verbose_name_plural = u'信息汇总'

    def __str__(self):
        return self.name.name.encode('utf-8')
