# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
from util.util import export_excel


# Register your models here.


class StaffInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_information')
    actions = ['export_action']

    def export_action(self, request, queryset):
        export_excel(queryset)
        self.message_user(request, "export OK!")

    export_action.short_description = "export Excel"


class PositionInfoAdmin(admin.ModelAdmin):
    list_display = ('positions', 'department')


admin.site.register(StaffInfo, StaffInfoAdmin)
admin.site.register(PositionInfo, PositionInfoAdmin)
admin.site.register(DepartmentInfo)
admin.site.register(BaseInfo, BaseInfoAdmin)