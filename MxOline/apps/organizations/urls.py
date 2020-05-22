from django.conf.urls import url
from django.urls import path, re_path
from apps.organizations.views import *

urlpatterns = [
    # 配置授课机构列表展示
    re_path('^list/$', OrgView.as_view(), name='org_list'),
    re_path('^ask/$', OrgAskView.as_view(), name='org_ask'),
    re_path(r'^(?P<org_id>\d+)/$', OrgDetailView.as_view(), name='org_detail'),
    re_path(r'^(?P<org_id>\d+)/detail-D/$', OrgDescDetailView.as_view(), name='detail_d'),
    re_path(r'^(?P<org_id>\d+)/detail-C/$', OrgCourseDetailView.as_view(), name='detail_c'),
    re_path(r'^(?P<org_id>\d+)/detail-T/$', OrgTeacherDetailView.as_view(), name='detail_t'),
    re_path('^teacher_list/$', TeacherView.as_view(), name='teacher_list'),
    re_path('^teacher_detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

]
