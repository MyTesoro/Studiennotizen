# from django.contrib import admin
# from apps.users.models import UserProfile
#
#
# # Register your models here.
#
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(UserProfile, UserProfileAdmin)

# 由于用户表比较特殊，为系统中存在的，Django内置了一个UserAdmin对显示用户信息做了优化
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from apps.users.models import UserProfile

admin.site.register(UserProfile, UserAdmin)
