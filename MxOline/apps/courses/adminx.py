import xadmin
from apps.courses.models import Course


# Register your models here.
# 无需继承admin.ModelAdmin
class CourseAdmin(object):
    # 显示字段
    list_display = ["id", "name", "desc", "learn_times", "degree"]
    # 搜索字段
    search_fields = ["name"]
    # 过滤器
    list_filter = ["id", "name", "desc", "learn_times", "degree"]


xadmin.site.register(Course, CourseAdmin)
