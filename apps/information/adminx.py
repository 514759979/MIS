import xadmin

from .models import *


# Register your models here.


class StaffInfoAdmin(object):
    list_display = ('name', 'department')


class BaseInfoAdmin(object):
    list_display = ('name', 'contact_information')  #显示字段
    search_fields = ('name', 'contact_information')  #搜索字段
    list_filter = ('name',)   #过滤器的字段


class PositionInfoAdmin(object):
    list_display = ('positions', 'department')


class DepartmentsAdmin(object):
    list_display = ('departments',)


xadmin.site.register(StaffInfo, StaffInfoAdmin)
xadmin.site.register(PositionInfo, PositionInfoAdmin)
xadmin.site.register(DepartmentInfo, DepartmentsAdmin)
xadmin.site.register(BaseInfo, BaseInfoAdmin)
