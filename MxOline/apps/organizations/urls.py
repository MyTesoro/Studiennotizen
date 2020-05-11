from django.urls import path,re_path
from apps.organizations.views import OrgView,OrgAskView

urlpatterns = [
    # 配置授课机构列表展示
    re_path('^list/', OrgView.as_view(), name='org_list'),
    re_path('^ask/', OrgAskView.as_view(), name='org_ask'),
]
