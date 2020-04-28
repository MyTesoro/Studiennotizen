import xadmin
from apps.organizations.models import *


# Register your models here.
# 无需继承admin.ModelAdmin
class CourseOrgAdmin(object):
    # 显示字段
    list_display = ["org_name", "org_tag", "students", "city", "courses_num"]
    # 搜索字段
    search_fields = ["org_name", "org_tag"]
    # 过滤器
    list_filter = ["org_tag", "students", "city", "courses_num", "click_nums", "org_category"]


class CityAdmin(object):
    # 显示字段
    list_display = ["city_name", "desc"]
    # 搜索字段
    search_fields = ["city_name", "desc"]
    # 过滤器
    list_filter = ["city_name"]


class TeacherAdmin(object):
    # 显示字段
    list_display = ["teacher_name", "work_company", "work_experience", "age", "affiliation"]
    # 搜索字段
    search_fields = ["teacher_name", "work_company", "work_experience", "age"]
    # 过滤器
    list_filter = ["teacher_name", "work_company", "work_experience", "age", "click_nums"]


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)
