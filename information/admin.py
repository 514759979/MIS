# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.


class StaffInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_information')


class PositionInfoAdmin(admin.ModelAdmin):
    list_display = ('positions', 'department')


admin.site.register(StaffInfo, StaffInfoAdmin)
admin.site.register(PositionInfo, PositionInfoAdmin)
admin.site.register(DepartmentInfo)
admin.site.register(BaseInfo, BaseInfoAdmin)