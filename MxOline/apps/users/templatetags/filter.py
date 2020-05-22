from django.template import Library
from django.contrib.auth.models import Group

# 创建一个Library类的实例对象
register = Library()


# 带一个参数的过滤器
@register.filter
def group_name(value, num):
    groupname = Group.objects.filter(user=num)[0]
    return groupname



